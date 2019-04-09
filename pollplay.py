import select
import socket

HOST='localhost'
PORT=6565
ADDR=(HOST,PORT)
skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind(ADDR)
skt.listen(5)

rlist=[skt]
wlist=[]
elist=[skt]
rl,wl,el=select.