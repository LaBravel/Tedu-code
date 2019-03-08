class Staff :
    '这是一个员工类'
    '这是类中第二个不赋值的字符串'

    __slots__ = ['no','name','position']

    def __init__(self,no,name,position) :
        self.no = no
        self.name = name
        self.position = position
        # self.salary = 8000
    
    def __str__(self) :
        ret = '编号:%s,名称:%s,职位:%s'\
         % (self.no,self.name,self.position)
        return ret

    def work(self) :
        print('%s正在工作' % self.name)


class ServiceRobot(Staff) :
    def __init__(self,no,name,position) :
        super().__init__(no,name,position)
    
    def work(self) :
        print('%s的工作,扫地' % self.name)

if __name__ == '__main__' :
    staff = Staff('0001','Jerry','经理')
    print(staff)
    robot = ServiceRobot('0002','aaaa','服务员')
    robot.work()