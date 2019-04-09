import socket
import select
import threading

HOST='localhost'
PORT=7777
ADDR=(HOST,PORT)
skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind(ADDR)
skt.listen(5)

def sendmsg():
    global rlist
    while True:
        my_msg=input()
        for r in rlist[1:]:
            r.send(my_msg.encode())


rlist=[skt]
wlist=[]
elist=[skt]
ndict={}
t=threading.Thread(target=sendmsg)
t.start()
while True:
    rl,wl,el = select.select(rlist,wlist,elist)
    for r in rl[:]:
        if r is skt:
            sk=skt.accept()
            rlist.append(sk[0])
        else:
            try:
                msg=r.recv(1024).decode()
                if msg[:5]=='name ':
                    ndict[r.fileno()]=msg[5:]
                    for user in rlist[1:]:
                        user.send((msg[5:]+' 加入了聊天室！！！').encode())
                else:
                    for user in rlist[1:]:
                        if user != r:
                            user.send((ndict[user.fileno()]+':'+msg).encode())

            except ConnectionResetError:
                for user in rlist[1:]:
                    if user != r:
                        user.send((ndict[r.fileno()]+'离开了聊天室！').encode())
                del ndict[r.fileno()]
                rlist.remove(r)
                r.close()
