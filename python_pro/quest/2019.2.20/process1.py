import multiprocessing as mp
from time import sleep

a = 1

def fun() :
    global a
    sleep(3)
    a = 1000
    print(a)
    print('子进程执行')

p = mp.Process(target = fun)
p.start()
sleep(2)
print('父进程执行')
p.join()
print(a)