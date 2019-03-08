class Mylist :
    def __init__(self,list) :
        self.list = list
        # self.lenth = len(list)

    def __str__(self) :
        ret = ''
        for i in self.list :
            ret += str(i) + ' '
        return ret 
    
    def __gt__(self,value) :
        if self.lenth == value.lenth :
            for i in range(self.lenth) :
                if self.list[i] > value.list[i] :
                    return True
            return False
        else :
            for i in range(min(self.lenth,value.lenth)) :
                if self.list[i] > value.list[i] :
                    return True
            if self.lenth > value.lenth :
                return True
            return False
    
    def __eq__(self,value) :
        if self.lenth == value.lenth :
            for i in range(self.lenth) :
                if self.list[i] != value.list[i] :
                    return False
            return True
        return False
    
    def __neg__(self) :
        return Mylist(-x for x in self.list)

    def __contains__(self,elements) :
        print('__contains__被调用')
        return elements in self.list
    
    def __getitem__(self,i) :
        return self.list[i]

    def __setitem__(self,i,value) :
        self.list[i] = value


L1 = Mylist([1,2,3])
L2 = Mylist([4,5,6])
