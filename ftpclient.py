import socket

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.connect(('localhost', 8888))
while True:
    msg=input()
    if not msg:
        skt.close()
        break
    skt.send('msg'.encode())
    data=skt.recv(1024)
    print(data.decode())