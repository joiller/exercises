import socket
import threading

HOST='localhost'
PORT=7777
ADDR=(HOST,PORT)
skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def sendmsg(skt):
    while True:
        message=input('you wanna say:')
        if not message:
            skt.close()
        skt.send(message.encode())

def setname(skt):
    name = input('name:')
    skt.send(('name ' + name).encode())

def recvmsg(skt):
    while True:
        data=skt.recv(1024)
        print(data.decode())


name = input('name:')
skt.connect(ADDR)
skt.send(('name ' + name).encode())

t2=threading.Thread(target=sendmsg,args=(skt,))
t3=threading.Thread(target=recvmsg,args=(skt,))
t2.setDaemon(True)
t3.setDaemon(True)
t3.start()
t2.start()
while True:
    pass