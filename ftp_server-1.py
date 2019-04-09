import select
import socket

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST='localhost'
PORT=8888
ADDR=(HOST,PORT)
skt.bind(ADDR)
skt.listen(5)

rlist=[skt]
wlist=[]
xlist=[skt]

choices='''请选择要下载的文件
1、吴宣仪
2、空姐
3、大长腿'''


def do_choice(sk):
    sk.send(choices.encode())


while True:
    rl,wl,xl=select.select(rlist,wlist,xlist)
    for r in rl:    # type:socket.socket
        if r==skt:
            sk,addr=skt.accept()
            rlist.append(sk)
        else:
            data=r.recv(1024).decode()
            if data[0]=='Q':
                r.close()
                rlist.remove(r)
                print(str(r.fileno())+'退出了')
            elif data[0]=='C':
                do_choice(r)
            elif data[0]=='1':
                wxy='吴宣仪吴宣仪吴宣仪吴宣仪'
                r.send(wxy.encode())
            elif data[0]=='2':
                wxy='空姐空姐空姐空姐空姐'
                r.send(wxy.encode())
            elif data[0]=='3':
                wxy='大长腿大长腿大长腿大长腿'
                r.send(wxy.encode())