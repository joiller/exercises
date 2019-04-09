import socket
import time


HOST='localhost'
PORT=7777
ADDRESS=(HOST,PORT)

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

skt.bind(ADDRESS)

skt.listen()

sk,adr=skt.accept()
print('i get :',adr)
data=sk.recv(1024)
print(data.decode())
