from socket import *
from select import *

#创建要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',1024))
s.listen(5)

#创建poll对象
p = epoll()

#建立查找字典
fdmap = {s.fileno():s}

#注册IO
p.register(s,EPOLLIN|EPOLLERR)

#循环监控
while True :
    events = p.poll() #阻塞
    for fd,event in events : #遍历列表，处理IO
        if fd == s.fileno() :
            c,addr = fdmap[fd].accept()
            print('Connect from:',addr)
            p.register(c,EPOLLIN|EPOLLHUP) #添加新的注册IO
            fdmap[c.fileno()] = c   
        elif event & EPOLLIN :
            data = fdmap[fd].recv(1024)
            if not data :
                print('客户端断开')
                p.unregister(fd) #取消关注
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print('Recvive:',data.decode())
            fdmap[fd].send(b'Thanks U')