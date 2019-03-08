from threading import Thread
from time import sleep,ctime

class Mythread(Thread) :
    def __init__(self,target = None,args = (),kwargs = {},name = ' ') :
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.name = name
    def run(self) :
        self.target(*self.args,**self.kwargs)

def player(sec,song) :
    for i in range(2) :
        print('Plying %s %s' % (song,ctime()))
        sleep(sec)

t = Mythread(target = player,args = (3,),kwargs = {'song':'lalala'},\
    name = 'happy')
t.start()
t.join()


