class Account :
    def __init__(self,acct_no,acct_name,reg_date,
    acct_type,acct_status = 'normal',balance = 0) :
        self.acct_no = acct_no
        self.acct_name = acct_name
        self.reg_date = reg_date
        self.acct_type = acct_type
        self.acct_status = acct_status
        self.balance = balance
        self.choice = 0
    
    def main(self) :  
        try :    
            if self.acct_status == 'loss' :
                print('操作失败,账户已经挂失')
                raise OSError
            if self.acct_status == 'freeze' :
                if self.choice == 'diposite' :
                    return
                print('操作失败,账户已经冻结')
                raise OSError 
        except OSError :
            print('操作失败,程序退出')
 
    def myprint(self) :
        print('账户账号:',self.acct_no)
        print('账户名称:',self.acct_name)
        print('开户日期:',self.reg_date)
        print('帐号类型:',self.acct_type)
        print('帐号状态:',self.acct_status)
        print('帐号余额:',self.balance)
    
    def diposite(self,num) :
        Account.myprint(self)
        self.choice = 'diposite'
        Account.main(self)
        self.balance += num
        print('存款成功\n当前账户余额:%d' % (self.balance))
    
    def draw(self,num) :
        Account.myprint(self)
        self.choice = 'draw'
        Account.main(self)
        if num <= self.balance :
            self.balance -= num
            print('取款成功\n当前账户余额:%d' % (self.balance))
        else :
            print('余额不足!')

    def freeze(self) :
        self.acct_status = 'freeze'
        Account.myprint(self)
        print('帐户冻结成功')

    def unfreeze(self) :
        self.acct_status = 'normal'
        Account.myprint(self)
        print('账户解冻成功')

    def report_loss(self) :
        self.acct_status = 'loss'
        Account.myprint(self)
        print('账户挂失成功')

    def relieve_loss(self) :
        self.acct_status = 'loss'
        Account.myprint(self)
        print('账户解挂失成功')
