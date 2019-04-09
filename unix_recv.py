import socket
import os

ADDR='./sockfile'

try:
    os.unlink(ADDR)

except OSError:
    if os.path.exists(ADDR):
        raise

skt=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
skt.bind(ADDR)      #进程中传输时，绑定文件名字
skt.listen(5)

while True:
    sk,addr=skt.accept()
    print('addr:',addr)
    while True:
        data=sk.recv(1024)
        print(data.decode())
        sk.send('nihao'.encode())