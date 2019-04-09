import threading
import socket
import os

HOST='localhost'
PORT=7777
ADDR=(HOST,PORT)

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind(ADDR)
skt.listen(5)
filelist=os.listdir(r'G:\adata')
class FTP:
    def __init__(self,sk):
        self.sk=sk

    def isend(self):
        for i in filelist:
            self.sk.send((i+'\n').encode())
            print('i send ',i)
        self.sk.send('ok'.encode())

    def irecv(self):
        while True:
            data=self.sk.recv(1024)
            return data.decode()

    def igive(self,file):
        with open(r'G:\adata'+'\\'+file,'r') as f:
            fdata=f.read(1024)
            fsend=self.sk.send(fdata.encode())
            self.sk.send('ok')
            print('i send a file:',file)



def sendmsg(sk):
    sk.send('halo'.encode())
    ftp=FTP(sk)
    while True:
        data = ftp.irecv()
        if data=='G':
            print('i got G')
            ftp.isend()

        elif data in filelist:
            ftp.igive(data)





while True:
    sk,addr=skt.accept()
    t=threading.Thread(target=sendmsg,args=(sk,))
    t.setDaemon(True)
    t.start()