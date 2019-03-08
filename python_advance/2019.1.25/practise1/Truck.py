class Truck :
    def __init__(self,load) :
        self.load = load

    def __add__(self,value) :
        print('add被调用')
        return Truck(self.load + value)
    
    def __str__(self) :
        return 'load:%d' % self.load

    def __mul__(self,value) :
        return Truck(self.load * value)     

    def __gt__(self,value) :
        if self.load > value :
            return True
        else :
            return False

    def __lt__(self,value) :
        if self.load < value :
            return True
        else :
            return False      

if __name__ == '__main__' :
    t1 = Truck(20)
    t2 = Truck(25)
    print(t1 > t2)
    print(t1 < t2)
    # t2 = t + 1
    # print(t2)
    # t3 = t * 4
    # print(t3)

