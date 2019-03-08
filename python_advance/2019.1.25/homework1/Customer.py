class Customer :
    def __init__(self,cust_id,cust_name,tel_no) :
        self.cust_id = cust_id
        self.cust_id = cust_name
        self.tel_no = tel_no
    
    def __str__(self) :
        a = '客户编号:%d\n' % self.cust_id
        b = '客户姓名:%d\n' % self.cust_name
        c = '客户电话:%d' % self.tel_no
        return a + b + c

Customer1 = Customer('01','Tom','123454321')
Customer2 = Customer('02','john','555555555')
Customer3 = Customer('03','Jack','010101010')