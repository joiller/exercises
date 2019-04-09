import socketserver

class Server(socketserver.ThreadingMixIn,socketserver.UDPServer):
    pass


class Handler(socketserver.DatagramRequestHandler):
    def handle(self):
        data=self.rfile.readline()
        print('i get a message:',data.decode())
        self.wfile.write('i get a message'.encode())

HOST='localhost'
PORT=8888
ADDR=(HOST,PORT)
server=Server(ADDR,Handler)
server.serve_forever()