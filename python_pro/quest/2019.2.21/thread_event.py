from threading import Thread,Event
from time import sleep

s = None #全局变量，用于通信
e = Event()
def foo() :
    print('Foooooooooooo')
    global s
    s = 'FFFFFFF'
    e.set()

f = Thread(target = foo)
f.start()

#主线程验证口令
print('口令')
e.wait()
if s == 'FFFFFFF' :
    print('Right')
else :
    print('Wrong')

f.join()