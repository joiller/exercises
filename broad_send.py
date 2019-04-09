import socket
import time

HOST='localhost'
PORT=7777
ADDR=(HOST,PORT)
dest=ADDR
skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    time.sleep(2)
    skt.sendto('nimenhao'.encode(),dest)
    data,addr=skt.recvfrom(1024)
    print(data.decode())
