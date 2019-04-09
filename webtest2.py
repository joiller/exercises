import socket
import time


HOST='localhost'
PORT=7777
ADDRESS=(HOST,PORT)

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sk.connect(ADDRESS)

data=sk.send('我连接到你了！'.encode())
print('我发送了：',data)
data1=sk.recv(1024)
print('我收到了：',data1.decode())
sk.close()