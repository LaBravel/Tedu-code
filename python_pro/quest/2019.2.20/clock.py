from multiprocessing import Process
import time

#自定义进程类
class ClockProcess(Process) :
    def __init__(self,value) :
        self.value = value
        super().__init__()
    
    def run(self) : #重写run方法
        for i in range(5) :
            print('The time is %s' % time.ctime())
            time.sleep(self.value)

p = ClockProcess(2) #创建进程对象
p.start() #启动新的进程
p.join()