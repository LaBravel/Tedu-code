from multiprocessing import Process
from time import sleep

#带参数进程函数
def worker(sec,name) :
    for i in range(3) :
        sleep(sec)
        print('I am %s' % name)
        print('I am working')

p = Process(target = worker,kwargs = {'name':'Tom'},\
            args = (2,))
p.start()
p.join()