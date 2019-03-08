from select import select 
from socket import *
import sys
from time import ctime

s = socket()
s.bind(('0.0.0.0',1024))
s.listen(3)

f = open('log.txt','a')

rlist = [s,sys.stdin]
wlist = []
xlist = []

while True :
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs :
        if r is s :
            c,addr = r.accept()
            rlist.append(c)
        elif r is sys.stdin :
            f.write('%s  %s  \n' % (ctime(),r.readline()))
            f.flush()
        else :
            data = c.recv(1024)
            if not data :
                rlist.remove(c)
                r.close()
                continue
            f.write('%s  %s  \n' % (ctime(),data.decode()))
            f.flush()
