from threading import Thread
from time import sleep

def fun(sec,name) :
    sleep(sec)
    print('%s 线程执行完毕' % name)

#创建多个线程
threads = []
for i in range(5) :
    t = Thread(target = fun,args = (2,),\
                kwargs = {'name':'T%d' % i})
    threads.append(t)
    t.start()

for i in threads :
    i.join()