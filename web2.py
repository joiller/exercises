import socket

cl=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cl.connect(('127.0.0.1',7777))
while True:
    talk=input('i wanna send you:')
    data=cl.send(talk.encode())
    if not data:
        cl.close()
        break
    print('i send a message:',data)

    data1=cl.recv(1024)

    print('i get message:',data1.decode())