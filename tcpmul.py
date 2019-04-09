import multiprocessing
import os
import socket
import signal

HOST='127.0.0.1'
PORT=9999
ADDR=(HOST,PORT)

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
skt.bind(ADDR)
skt.listen(5)

def link(sk,addr):
    print('linking to',addr)
    while True:
        data=sk.recv(1024)
        if not data:
            sk.close()
            break
        print('i get a message:',data,'from',addr)
        data1=sk.send('i get your messages!'.encode())
        print('i send a message:to',addr)

if __name__ == '__main__':
    ps=[]
    while True:
        sk, addr = skt.accept()
        p=multiprocessing.Process(target=link,args=(sk,addr))
        p.daemon=True
        p.start()
        ps.append(p)

