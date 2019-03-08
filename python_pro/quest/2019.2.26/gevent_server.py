from socket import *
from gevent import monkey
import gevent
monkey.patch_all()

def server() :
    s = socket()
    s.bind(('0.0.0.0',1024))
    s.listen(5)
    while True :
        c,addr = s.accept()
        print('Connect from',c)
        gevent.spawn(handle,c)
    
def handle(c) :
    while True :
        data = c.recv(1024)
        if not data :
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

server()