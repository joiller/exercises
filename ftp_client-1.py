import socket
import threading

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST='localhost'
PORT=8888
ADDR=(HOST,PORT)
skt.connect(ADDR)


def main():
    while True:
        msg=input('''请输入要进行的操作
        1、输入Q退出
        2、输入其他下载''')
        if msg=='Q':
            skt.send(msg.encode())
            skt.close()
            break
        else:
            skt.send(msg.encode())
            data=skt.recv(1024).decode()
            return scene2(data)


def down(skt):
    downed=skt.recv(1024).decode()
    with open(r'G:\python\homework\ftp1.txt','w') as f:
        f.write(downed)


def scene2(data):
    while True:
        msg=input(data)
        if msg=='Q':
            return main()
        else:
            skt.send(msg.encode())
            t=threading.Thread(target=down(skt))
            t.setDaemon(True)


main()