class Ellipse :#定义为椭圆
    #类中的函数，称之为方法
    def __init__(self,a,b) :
        self.a = a#属性：短半径
        self.b = b#属性：长半径
    def calc_len(self) :
        return 2 * 3.14 * self.b + \
                4 * (self.b - self.a)
    def calc_area(self) :#计算面积
        return 3.14 * self.a * self.b

e = Ellipse(2.0,3.0)#实例化，创建椭圆对象
len = e.calc_len()#计算周长
area = e.calc_area()#获得椭圆面积
print('短半径:%f,长半径:%f,len=%f,area=%f' 
    % (e.a,e.b,len,area))