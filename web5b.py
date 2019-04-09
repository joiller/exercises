import socket

HOST='localhost'
PORT=6666
ADDRESS=(HOST,PORT)


skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data=skt.sendto('hahaha'.encode(),ADDRESS)


print('i send message',data)