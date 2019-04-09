import gevent.monkey
gevent.monkey.patch_all()
import socket

HOST='localhost'
PORT=7777
ADDRESS=(HOST,PORT)
skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind(ADDRESS)
skt.listen(5)


def what(sk):
    print('linking to',sk.getpeername())
    while True:
        data=sk.recv(1024)
        if not data:
            break
        print('the message is:',data.decode())
        sk.send('i received your message!'.encode())
    sk.close()


while True:
    sk,addr=skt.accept()
    g=gevent.spawn(what,sk)