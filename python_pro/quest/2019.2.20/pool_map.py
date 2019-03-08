from multiprocessing import Pool
from time import sleep,ctime

def func(n) :
    sleep(1)
    return n * n

p = Pool()
r = p.map(func,range(10))
p.close()
p.join()


print(r)