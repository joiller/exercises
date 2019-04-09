import socket
import os


ADDR='./sockfile'
skt=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
skt.connect(ADDR)

while True:
    skt.send('halo'.encode())
    data=skt.recv(1024)
    print('i got a message:',data.decode())