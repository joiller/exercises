import socket
import multiprocessing
import time

skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ADDR=('localhost',2333)
skt.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# skt.bind(ADDR)


def write(skt):
    # print('writing')
    while True:
        data=input()
        if not data:
            skt.sendto('Q'.encode(),ADDR)
            break
        else:
            skt.sendto(('C'+data).encode(),ADDR)


def get(skt):
    # print('receiving')
    while True:
        print('receiving')
        msg,addr = skt.recvfrom(1024)
        if msg.decode()[0] == 'Q':
            break
        print(msg.decode())


if __name__ == '__main__':

    while True:
        name = input('请输入名字')
        skt.sendto(('L' + name).encode(), ADDR)
        nmsg, addr = skt.recvfrom(1024)
        if nmsg.decode() == '用户名已存在':
            print(nmsg.decode())
        else:
            print(nmsg.decode())
            break

    # windows不能实现子进程在cmd中输入
    # t1=multiprocessing.Process(target=write,args=(skt,))
    t2=multiprocessing.Process(target=get,args=(skt,))
    # print('t2进程开启')
    # t1.start()
    t2.start()
    # print('t2运行')
    time.sleep(1)   # write是个阻断函数，可能导致t2进程还没有真的开始就被阻断了
    write(skt)
    # t1.join()
    t2.join()