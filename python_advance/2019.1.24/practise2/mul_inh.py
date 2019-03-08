class Fighter :
    def fight(self) :
        print('我能战斗')

class Flyer :
    def fly(self) :
        print('我会飞')

class Firer :
    def fire(self) :
        print('我能喷火')

class SuperMan(Fighter,Flyer,Firer) :
    pass

super_man = SuperMan()
super_man.fight()
super_man.fly()
super_man.fire()