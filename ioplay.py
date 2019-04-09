import socket
import select


HOST='localhost'
PORT=8888
ADDR=(HOST,PORT)
skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind(ADDR)
skt.listen(5)

rlist=[skt]
wlist=[]
xlist=[skt]
while True:
    rs,ws,xs=select.select(rlist,wlist,xlist)
    print('sth happened')
    for r in rs:
        if r == skt:
            print(r,'happened')
            sk,addr=r.accept()
            print('linking to ',addr)
            rlist.append(sk)
        else:
            data=r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print('i get a message:',data)
                r.send('i get your message'.encode())