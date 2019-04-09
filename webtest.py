import socket
import time

HOST='localhost'
PORT=7777
ADDRESS=(HOST,PORT)

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

skt.bind(ADDRESS)

skt.listen(10)
print('可以连接')
print('准备接收连接')
sk,adr=skt.accept()
print('已经连接：',adr)
print('准备接收消息')

data=sk.recv(1024)
print('收到消息：',data.decode())

data1=sk.send('i get you message'.encode())
print('已发送消息：',data1)


sk.close()
skt.close()