import socket
import multiprocessing
import os
import signal

HOST='localhost'
PORT=6666
ADDR=(HOST,PORT)

skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
skt.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
skt.bind(ADDR)

def recv(skt):
    data,addr=skt.recvfrom(1024)
    print('i get message:',data,'from',addr)


if __name__ == '__main__':

    ps=[]
    for i in range(3):
        p=multiprocessing.Process(target=recv,args=(skt,))
        ps.append(p)
        p.start()

    for p in ps:
        p.join()