import socket
import time
import select
import threading


skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind(('localhost',7777))
skt.listen(5)
rlist=[skt]
wlist=[]
elist=[]

while True:
    rl,wl,el=select.select(rlist,wlist,elist)
    for r in rl:
        if r is skt:
            sk,addr=skt.accept()
            rlist.append(sk)
        else:
            try:
                data=r.recv(1024)
                print(data.decode())
                r.send('gotcha'.encode())
            except ConnectionResetError:
                rlist.remove(r)
                r.close()
                break