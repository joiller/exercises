import socket

#创建一个socket对象
skfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定IP和端口号
skfd.bind(('127.0.0.1',7777))

#将套接字变为监听套接字
skfd.listen(10)

L=[]
i=0
while True:
    print('waiting for connect...')
    #等待客户端请求
    sk1,adr1=skfd.accept()
    print('i get address:',adr1)
    while True:
        #接收客户端的消息
        data=sk1.recv(1024)
        if not data:
            break
        print('i get message:',data.decode())

        #给客户端发送消息
        data1=sk1.send('i wanna be a bytes'.encode())
        print('i send message:',data1)
        print('已经进行了', i + 1, '次收发工作')
        i += 1
        #关闭套接字
    sk1.close()      #与该客户端断开连接（四次挥手）


    # skfd.close()     #关闭socket套接字