from practise2 import *
class Car(AutoMobile) :
    pass

if __name__ == '__main__' :
    mycar = Car('小汽车','蓝色',1.40)
    mycar.startup()
    mycar.run()
    mycar.stop()
    mycar.info()