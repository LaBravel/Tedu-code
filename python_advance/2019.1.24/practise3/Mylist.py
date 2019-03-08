class Mylist :
    def __init__(self,iterable = []) :
        self.date = [x for x in iterable]

    def __str__(self) :
        ret = ''
        for x in self.date :
            ret += str(x) 
            ret += ' '
        return ret

    def __len__(self) :
        return Mylist(len(x) for x in self.date)

    def __reversed__(self) :
        a = reversed(self.date)
        r = ''
        for i in a :
            r += str(i) + ' '
        return r
getattr()
setattr()


L = [1,2,3,-4,-5,-6,7.34,8.76]
mylist = Mylist(L)
print(mylist)
print(reversed(mylist))