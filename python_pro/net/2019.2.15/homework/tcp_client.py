from socket import *

#创建套接字
sockfd = socket()

#发起连接
server_addr = ('127.0.0.1',1024)
sockfd.connect(server_addr)

while 1 :
    #收发消息
    data = input('>>')
    if not data :
        break
    sockfd.send(data.encode())
    #data = sockfd.recv(1024)
    #print('From server:',data.decode())

#关闭套接字
sockfd.close()