import socket
import sys
import re

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.connect(('localhost',7777))


def do_log():
    user=input('用户名:')
    pwd=input('密码:')
    skt.send(('L'+user+'\t'+pwd).encode())
    yes = skt.recv(1024).decode()
    if yes == 'yes':
        return 'yes'
    elif yes == 'user':
        return 'user'
    elif yes == 'no':
        return 'no'

def do_sign():
    while True:
        print('输入\'Q\'退出注册')
        user = input('用户名')
        pwd = input('密码')
        pwd2 = input('确认密码')
        ums = re.findall(r'\s',user)
        pms = re.findall(r'\s',pwd)
        if pwd != pwd2:
            print('两次密码不一致')
        elif len(ums) != 0 or len(pms) != 0:
            print('用户名和密码不能有空字符串')
        elif user == 'Q' or pwd == 'Q' or pwd2 == 'Q':
            return
        else:
            skt.send(('I'+user+'\t'+pwd).encode())
            msg = skt.recv(1024).decode()
            print(msg)
            if msg == 'exist':
                print('用户名已存在')
                return 'no'
            elif msg == 'ok':
                print('注册成功')
                return 'yes'
            else:
                print('recv到了奇怪的东西')

def do_search():
    search_word = input('请输入要查询的单词（输入\'Q\'返回上一界面）：')
    if search_word != 'Q':
        skt.send(('S'+search_word).encode())
        search_result = skt.recv(1024).decode()
        print(search_result)
    else:
        second()


# 第一界面
def first():
    while True:
        data=input('注册：Sign up/登录：Login/退出：Quit')
        if data=='S':   # 注册
            # skt.send('Si'.encode())
            s = do_sign() # 判断是否注册成功

        elif data == 'L':  # 登录
            # skt.send('L'.encode())
            l = do_log()   # 判断是否登录成功
            if l == 'yes':  # 跳转至第二界面
                print('登录成功！')
                second()
            elif l == 'user':
                print('用户名不存在！')
            elif l == 'no':
                print('密码错误！')
        elif data == 'Q':  # 退出程序
            skt.send('Q'.encode())
            sys.exit()
        else:
            print('输入有误')


# 第二界面
def second():
    while True:
        msg=input('查询：S/历史记录：H/返回主界面：B')
        if msg == 'S':
            do_search()
        elif msg == 'H':
            skt.send('H'.encode())
            while True:
                rec=skt.recv(1024).decode()
                if rec == 'send over':
                    break
                skt.send('one'.encode())
                print(rec)
                print('下一条')
        elif msg == 'B':
            first()


if __name__ == '__main__':
    first()