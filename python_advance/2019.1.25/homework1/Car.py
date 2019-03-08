class Car :
    def __init__(self,car_id,name,is_lend,price,start_date,end_date) :
        self.car_id = car_id
        self.name = name
        self.is_lend = is_lend
        self.price = price
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self) :
        a = '车辆编号:%s\n' % self.car_id
        b = '车辆名称:%s\n' % self.name
        c = '是否出租:%s\n' % self.is_lend
        d = '每天单价:%d\n' % self.price 
        e = '起租日期:%s\n' % self.start_date
        f = '还车日期:%s' % self.end_date
        return a + b + c +  d + e + f

Car1 = Car('001','本田','未出租',1500,'','')
Car2 = Car('002','铃木','已出租',2000,'2018.12.1','2019.1.31')
Car3 = Car('003','沃尔沃','已出租',2500,'2018.12.15','2019.1.15')

