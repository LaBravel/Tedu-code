'''
HTTP Server v2.0
*多线程并发
*基本的request解析
*能够反馈基本数据
*使用类封装
'''

from socket import *
from threading import Thread
import sys

#封装具体的类作为HTTP　server功能模块
class HTTPServer(object) :
    def __init__(self,server_addr,static_dir) :
        self.server_addr = server_addr
        self.create_socket()
        self.bind()
        self.static_dir = static_dir
    def create_socket(self) :
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    def bind(self) :
        self.sockfd.bind((self.server_addr))
        self.ip = self.server_addr[0]
        self.port = self.server_addr[1]
    def serve_forever(self) :
        self.sockfd.listen(5)
        print('Listen the port %d' % self.port)
        while True :
            try :
                c,addr = self.sockfd.accept()
            except KeyboardInterrupt :
                self.sockfd.close()
                sys.exit('退出程序')
            except Exception as e :
                print('Error',e)
            
            clientThread = Thread(target = self.handle,\
                        args = (c,))
            clientThread.setDeamon = True
            clientThread.start()   
    def handle(self,c) :
        request = c.recv(4096)
        if not request :
            c.close()
            return
        requestHeaders = request.splitlines()
        print(c.getpeername(),':',requestHeaders[0])  
        getRequest = str(requestHeaders[0]).split(' ')[1]
        
        if getRequest == '/' or getRequest[-5:] == '.html' :
            print('想获取网页')
            self.get_html(c,getRequest)
        else :
            print('想获取其它内容')   
    def get_html(self,c,getRequest) :
        if getRequest == '/' :
            filename = self.static_dir + '/index.html'
        else :
            filename = self.static_dir + getRequest
        print(filename)
        try :
            f = open(filename)
        except IOError : #没有找到网页
            responseHeaders = 'HTTP/1.1 404 Not Found\r\n'
            responseHeaders += '\r\n'
            responseBody = 'Sorry,Not found the page'
        else : #返回网页内容
            responseHeaders = 'HTTP/1.1 200 OK\r\n'
            responseHeaders += '\r\n'
            responseBody = f.read()
        finally :
            response = responseHeaders + responseBody
            c.send(response.encode())
    def get_data(self,c,getRequest) :
        responseHeaders = 'HTTP/1.1 200 OK\r\n'
        responseHeaders += '\r\n'
        responseBody = '<p>waiting httpserver v3.0</p>'
        response = responseHeaders + responseBody
        c.send(response.encode())
    

if __name__ == '__main__' :
    server_addr = ('0.0.0.0',1024) #使用者自己设定address
    static_dir = './static' #用户提供存放网页的目录
    httpd = HTTPServer(server_addr,static_dir) #创建服务器对象
    httpd.serve_forever() #启动服务