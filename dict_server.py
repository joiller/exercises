import select
import socket
import re
import pymysql


word_dict={}

with open(r'G:\资料类的\大学\day02\regex\dict.txt','r') as f:
    while True:
        word = f.readline()
        if word == '':
            break
        li = re.split(r'\s+',word,1)
        word_dict[li[0]]=li[1][0:-1]

print(word_dict['zygote'])

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind(('localhost',7777))
skt.listen(5)

rlist=[skt]
wlist=[]
xlist=[skt]


def do_sign(log_msg):
    print(log_msg)
    print(log_msg[1:])
    up = re.split(r'\t',log_msg[1:])
    print(up)
    db = pymysql.connect('localhost','root','jhl233666','pydict',charset='utf8')
    cur = db.cursor()
    sign_select = 'select user from user_info;'
    cur.execute(sign_select)
    users = cur.fetchall()
    for i in users:
        if up[0] == i[0]:
            return 'no'
    print('insert into user_info values'+'(\''+up[0]+'\',\''+up[1]+'\')'+';')
    cur.execute('insert into user_info values'+'(\''+up[0]+'\',\''+up[1]+'\')'+';')
    db.commit()
    cur.close()
    db.close()
    return 'yes'


def do_login(data,r):
    global now_users
    now_users = {}
    up = re.split(r'\t',data[1:])
    db = pymysql.connect('localhost', 'root', 'jhl233666', 'pydict', charset='utf8')
    cur = db.cursor()
    user_select = 'select user,pasw from user_info;'
    cur.execute(user_select)
    users = cur.fetchall()
    print(users)
    for i in users:
        if i[0] == up[0] and i[1] == up[1]:
            now_users[r]=up[0]
            print(now_users)
            return 'yes'
        elif i[0] == up[0] and i[1] != up[1]:
            return 'no'
    return 'user'

def do_search(data,r):
    global now_users
    search_word = data[1:]
    for key,value in word_dict.items():
        if search_word == key:
            r.send((str(key)+'\t'+str(value)).encode())
            db = pymysql.connect('localhost', 'root', 'jhl233666', 'pydict', charset='utf8')
            cur = db.cursor()
            add_hist = 'insert into hist values(\''+now_users[r]+'\',\''+str(key)+':'+str(value)+'\');'
            print(add_hist)
            cur.execute(add_hist)
            db.commit()
            cur.close()
            db.close()
            return True
    r.send('没有这个单词，查看是否拼写错误'.encode())


def do_hist(r):
    global now_users
    db = pymysql.connect('localhost', 'root', 'jhl233666', 'pydict', charset='utf8')
    cur = db.cursor()
    hists = 'select * from hist where user=\''+now_users[r]+'\''
    cur.execute(hists)
    hists_find=cur.fetchall()
    for i in hists_find:
        # print('start')
        r.send((str(i)).encode())
        m=r.recv(1024)
        # print(m.decode())
    r.send('send over'.encode())


def do_quit(r):
    r.close()
    rlist.remove(r)


while True:
    rl,wl,xl=select.select(rlist,wlist,xlist)
    for r in rl:  # type:socket.socket
        if r == skt:
            sk,addr = skt.accept()
            rlist.append(sk)
            

        else:
            data=r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                print('已经关闭一个连接',str(r.getpeername()))
                r.close()
            else:
                if data[0] == 'S':
                    do_search(data,r)

                elif data[0] == 'L':
                    yes = do_login(data,r)
                    if yes == 'yes':
                        r.send('yes'.encode())
                    elif yes == 'no':
                        r.send('no'.encode())
                    elif yes == 'user':
                        r.send('user'.encode())

                elif data[0] == 'I':
                    yes = do_sign(data)
                    if yes == 'no':
                        print('发送了exist')
                        r.send('exist'.encode())
                    elif yes == 'yes':
                        print('发送了ok')
                        r.send('ok'.encode())

                elif data[0] == 'H':
                    do_hist(r)

                else:
                    do_quit(r)