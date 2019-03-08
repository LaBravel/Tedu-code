import threading
from time import sleep
import os

#线程函数
def music() :
    for i in range(5) :
        sleep(2)
        print('播放1',os.getpid())

t = threading.Thread(target = music)
t.start()

for i in range(3) :
    sleep(3)
    print('播放2',os.getpid())

t.join()
print('Main thread a:',a)