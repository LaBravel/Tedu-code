'''
使用socketserver模块完成网络并发模型
'''

from socketserver import *

#创建tcp多进程并发模型
class Server(ForkingMixIn,TCPServer) :
    pass

#具体请求处理类
class Handler(StreamRequestHandler) :
    #重写具体处理方法
    def handle(self) :
        print('Connect from',self.client_address)
        while True :
            #self.request => accept返回的客户端connfd
            data = self.request.recv(1024)
            if not data :
                break
            print(data.decode())
            self.request.send(b'OK')

server_addr = ('0.0.0.0',1024)
server = Server(server_addr,Handler)
server.serve_forever() #启动服务
