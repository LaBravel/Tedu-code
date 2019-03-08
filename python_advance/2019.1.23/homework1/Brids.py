class Birds :
    def __init__(self,name,eat,fly,reproduc) :
        self.name = name
        self.eat = eat
        self.fly = fly
        self.reproduc = reproduc
    
    def Birds_name(self) :
        print('鸟类名称:',self.name)

    def Birds_eat(self) :
        print('好吃吗？',self.eat)

    def Birds_fly(self) :
        print('会飞吗?',self.fly)

    def Birds_reproduc(self) :
        print('我是%s,%s' % (self.name,self.reproduc))
        print('let`s fuck lol~')