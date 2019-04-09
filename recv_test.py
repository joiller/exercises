import socket


skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind(('localhost',8888))
skt.listen(5)
sk,addr=skt.accept()
while True:
    data=sk.recv(1024)
    if not data:
        sk.close()
        break
    else:
        print(data.decode())
        sk.send('halo'.encode())