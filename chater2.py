import socket
import threading
import time

HOST='localhost'
PORT=7777
ADDR=(HOST,PORT)
skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def sendmsg(skt):
    while True:
        message=input()
        if not message:
            skt.close()
            break
        else:
            skt.send(message.encode())


def setname(sk):
    name = input('name:')
    sk.send(('name ' + name).encode())


def recvmsg(skt):
    while True:
        time.sleep(1)
        try:
            data=skt.recv(1024)
            if not data:
                skt.close()
                break
            else:
                print(data.decode())
        except OSError:
            break


name = input('name:')
skt.connect(ADDR)
time.sleep(1)
skt.send(('name ' + name).encode())

t2=threading.Thread(target=sendmsg,args=(skt,))
t3=threading.Thread(target=recvmsg,args=(skt,))
# t2.setDaemon(True)
# t3.setDaemon(True)
t3.start()
t2.start()
t2.join()
t3.join()