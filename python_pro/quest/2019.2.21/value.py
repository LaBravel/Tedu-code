from multiprocessing import Process,Value
import time,random

#创建共享内存
money = Value('i',5000)

#操作共享内容
def boy() :
    for i in range(30) :
        time.sleep(0.2)
        money.value += random.randint(1,1000)

def girls() :
    for i in range(30) :
        time.sleep(0.16)
        money.value -= random.randint(100,900)

m = Process(target = boy)  
g = Process(target = girls)
m.start()
g.start()
m.join()
g.join()                                                                                                                                                                                                                                                                     
print(money.value)