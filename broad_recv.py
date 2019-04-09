import socket

HOST='localhost'
PORT=7777
ADDR=(HOST,PORT)
skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
skt.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
skt.bind(ADDR)

while True:
    try:
        data,addr=skt.recvfrom(1024)
        print('i get a message:',data.decode())
        skt.sendto('halo'.encode(),addr)

    except Exception as e:
        print(e)