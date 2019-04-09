import socket


HOST='localhost'
PORT=7777
ADDR=(HOST,PORT)
skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.connect(ADDR)

# while True:
name=skt.recv(1024)
    # if not name:
    #     break
print('i get the filename:',name.decode())
while True:
    xx=input('what to send')
    if not xx:
        break
    msg=skt.send(xx.encode())
    print('i have sent')
    while True:
        zz=skt.recv(1024)
        zz=zz.decode()
        if zz[-2:]=='ok':
            print(zz[:-2])
            break
        print(zz)

# while True:
    # if not data:
    #     break
print('i got data:', data.decode(),addr[0],addr[1])

skt.close()