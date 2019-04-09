import socket

skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
skt.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
skt.bind(('localhost',2333))
di={}

def do_login(msg,di,addr,skt):
    if len(di) == 0:
        di[addr] = msg[1:]
        skt.sendto('ok'.encode(),addr)
        # print(di)
    else:
        yes=True
        for key,value in di.items():
            if value == msg[1:]:
                skt.sendto('用户名已存在'.encode(),addr)
                yes = False
                break
        if yes:
            for key in di:
                skt.sendto(('%s加入了聊天室'%msg[1:]).encode(),key)
            di[addr] = msg[1:]
            skt.sendto('ok'.encode(),addr)
            # print('加入完毕')


def do_quit(di,addr,skt):
    my_msg=di[addr]
    skt.sendto('Q'.encode(),addr)
    del di[addr]
    for key in di:
        skt.sendto(('%s离开了聊天室'%my_msg).encode(),key)

    # print(di)


def do_chat(msg,di,addr,skt):
    # print('do_chat:',msg)
    for key in di:
        if key !=addr:
            # print(di[addr], key)
            skt.sendto((di[addr]+':'+msg[1:]).encode(), key)


while True:
    # print('receiving......')
    data,addr=skt.recvfrom(1024)
    # print('received')
    msg=data.decode()  # type:str
    if msg[0] == 'L':
        do_login(msg,di,addr,skt)

    elif msg[0] == 'Q':
        do_quit(di,addr,skt)

    else:
        do_chat(msg,di,addr,skt)