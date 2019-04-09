import socket
import time
# from webtest import ADDRESS


HOST='localhost'
PORT=7777
ADDRESS=(HOST,PORT)
skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

skt.connect(ADDRESS)

skt.send('hello world!'.encode())
data1=skt.recv(1024)
print('i get a message:',data1.decode())
skt.send('i love you'.encode())
data2=skt.recv(1024)
print('i get a message:',data2.decode())

skt.close()