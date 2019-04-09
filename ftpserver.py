import socket
import select

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind(('localhost',8888))
skt.listen(5)

rlist=[skt]
wlist=[]
xlist=[skt]

while True:
    rl,wl,xl=select.select(rlist,wlist,xlist)
    for r in rl[:]:
        if r is skt:
            sk,addr=skt.accept()
            rlist.append(sk)

        else:
            data=r.recv(1024)
            if not data:
                r.close()
                rlist.remove(r)
                break
            else:
                r.send('i got your msg'.encode())