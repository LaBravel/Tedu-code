class Mylist :
    def __init__(self,list) :
        self.list = list

    def __str__(self) :
        ret = ''
        for i in self.list :
            ret += str(i)
        return ret
    
    def __iadd__(self,list000) :
        return Mylist(self.list + list000.list)

    def __mul__(self,value) :
        return Mylist(self.list * value)

    def __gt__(self,value) :
        if self.list > value.list
            return True
        else :
            return False

    def __lt__(self,value) :
        if self.list < value.list
            return True
        else :
            return False
L1 = Mylist([1,2,3])
L2 = Mylist([4,5,6])
L1 += L2
print(L1)
print(L1 * 2)
print(L1　> L2)