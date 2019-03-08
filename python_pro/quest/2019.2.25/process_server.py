from socket import *
from multiprocessing import Process
import signal

#创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0,1024'))
s.listen(3)

#处理僵尸
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

#客户端处理函数
def handle(c) :
    print('Connect from',c.getpeername())
    while True :
        data = c.recv(1024)
        if not data :
            break
        print(data.decode())
        c.send(b'OK')
    c.close()
    sys.exit(0)

#循环等待客户端连接
while True :
    try :
        c,addr = s.accept()
    except KeyboardInterrupt :
        s.close()
        break
    except Exception as e :
        print(e)
        continue

    #创建线程处理客户端请求
    p = Process(target = handle,args = (c,))
    p.deamon = True #让分支线程随主线程退出
    p.start()