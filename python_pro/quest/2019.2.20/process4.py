from multiprocessing import Process
from time import sleep,ctime

def tm() :
    for i in range(3) :
        sleep(2)
        print(ctime())
    
p = Process(target = tm)
print(
    'Process Name:',p.name,'\n\r',
    'Process PID:',p.pid,'\n\r',
    'Process status',p.is_alive()
    )
p.daemon = True
p.start()
print(
    'Process Name:',p.name,'\n\r',
    'Process PID:',p.pid,'\n\r',
    'Process status',p.is_alive()
    )
p.join
