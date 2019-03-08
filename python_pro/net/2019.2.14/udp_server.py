from socket import *

#创建数据包套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
server_addr = ('0.0.0.0',8888)
sockfd.bind(server_addr)

#消息收发
while 1 :
    try :
        data,addr = sockfd.recvfrom(1024)
        print('Receive from %s:%s' % (addr,data.decode()))
        sockfd.sendto(b'thanks for your msg',addr)
    except KeyboardInterrupt :
        break

#关闭套接字
sockfd.close()