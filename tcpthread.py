import threading
import socket

HOST='localhost'
PORT=7777
ADDR=(HOST,PORT)

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
skt.bind(ADDR)
skt.listen(5)

def link(sk):
    print('linking to',sk.getpeername())
    while True:
        data = sk.recv(1024)
        if not data:
            sk.close()
            break
        print('i get a message:',data.decode())
        data1=sk.send('i love you'.encode())
        print('i send a message')

ts=[]
while True:
    sk,addr=skt.accept()
    t=threading.Thread(target=link,args=(sk,))
    t.start()
    ts.append(t)
