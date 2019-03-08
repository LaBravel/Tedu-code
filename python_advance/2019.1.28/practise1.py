class ChainStore :
    store_num = 0
    total_income = 0
    store_list = []

    def __init__(self,store_no,store_name,store_address,manager) :
        print('门店开张')
        self.store_no = store_no
        self.store_name = store_name
        self.store_address = store_address
        self.manger = manager
        self.myincome = 0
        ChainStore.store_num += 1
        ChainStore.store_list.append(self)

    def do_business(self,income) :
        print('正在营业')
        self.myincome += income
        ChainStore.total_income += income

    def __str__(self) :
        ret = '编号:%s,名称:%s,地址:%s,店长:%s,总营业额:%.2f'\
         % (self.store_no,self.store_name,self.store_address,
         self.manger,self.myincome)
        return ret
             

    @classmethod
    def print_total(cls) :#类方法，打印类的属性
        print('门店数量:%d,营业额度:%.2f,'\
            % (cls.store_num,cls.total_income))
        for store in cls.store_list :
            print(str(store))

    @staticmethod
    def print_regulation() :#静态方法打印管理条例
        regulation = '''
        ------------管理条例--------------
        1.考勤
        2.不迟到
        3.有事请假
        '''
        print(regulation)
    
if __name__== '__main__' :
    store1 = ChainStore('1','西单旗舰店','西单','David')
    store1.do_business(20000)
    print('门店数量:',ChainStore.store_num)
    print('总营业额:',ChainStore.total_income)
    print('')
    store2 = ChainStore('2','东单旗舰店','东单','DiDi')
    store2.do_business(25000)
    print('门店数量:',ChainStore.store_num)
    print('总营业额:',ChainStore.total_income)
    ChainStore.print_total()
    ChainStore.print_regulation()