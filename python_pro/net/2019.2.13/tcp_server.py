import socket

#创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0',6661))

#设置监听
sockfd.listen(5)

while 1 :
    #等待处理客户端连接
    print('Watting for connect')
    try :    
        connfd,addr = sockfd.accept()
    except KeyboardInterrupt :
        print('Server exit')
        break
    print('Connect from',addr)#客户端地址
    while 1 :
    #收发消息
        data = connfd.recv(1024)
        if not data :
            break
        print('Receive message:',data.decode())
        n = connfd.send(b'Receive your message!!')
        print('Send %d bytes' % n)
    

#关闭套接字
connfd.close()
sockfd.close()