from socket import *
from time import sleep,ctime

sockfd = socket()
sockfd.bind(('127.0.0.1',1024))
sockfd.listen(3)

#设置为非阻塞状态
sockfd.setblocking(False)
#设置为超时阻塞状态
sockfd.settimeout(10)

while True :
    print('Waiting for connect...')
    try :
        connfd,addr = sockfd.accept()
    except BlockingIOError :
        sleep(2)
        print('%s connect error' % ctime())
    except timeout :
        sleep(2)
        print('%s connect error' % ctime())
    else :
        print('Conncet from',addr)