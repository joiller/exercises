import socketserver

class Server(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass

class Handler(socketserver.StreamRequestHandler):
    #当有客户端连接时，调用该函数自动处理客户端的请求
    def handle(self):
        while True:
            data=self.request.recv(1024)
            if not data:
                print('over')
                break
            print('i get a message:',data)
            self.request.send('hahaha, igot you'.encode())

HOST='localhost'
PORT=8888
ADDR=(HOST,PORT)
server=Server(ADDR,Handler)

server.serve_forever()