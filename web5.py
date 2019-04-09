import socket

HOST='localhost'
PORT=7777
ADDRESS=(HOST,PORT)


skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

skt.bind(ADDRESS)

while True:

    data,adr=skt.recvfrom(1024)
    print('i get message:',data.decode(),'from',adr)