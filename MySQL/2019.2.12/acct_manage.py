from db_oper import DBOper

class Acct :
    def __init__(self,acct_no,acct_name,acct_type,balance) :
        self.acct_no = acct_no
        self.acct_name = acct_name
        self.acct_type = acct_type
        self.balance = balance

    def __str__(self) :
        ret = '帐号：%s,户名：%s,类型：%s,余额：%.2s' % (
            self.acct_no,self.acct_name,self.acct_type,self.balance)
        return ret

class AcctManage :
    def __init__(self,db_oper) :
        self.db_oper = db_oper
    
    def query_all_acct(self) :
        accts = []
        sql = 'select * from acct'
        result = self.db_oper.do_query(sql)
        if not result :
            print('查询结果为空')
            return None
        for r in result :
            acct_no = r[0]#帐号
            acct_name = r[1]#户名
            acct_type = r[3]#类型
            balance = r[6]#余额
            accts.append(Acct(acct_no,acct_name,acct_type,balance))
        return accts
        #返回结果，实例化一个Acct对象列表返回
    
    def query_by_id(self,acct_no) :#根据账户查询，最多返回一个Acct对象
        sql = 'select * from acct where acct_no = %s' % acct_no
        result = self.db_oper.do_query(sql)
        if not result :
            print('查询结果为空')
            return None
        r = result[0]
        return Acct(r[0],r[1],r[3],r[6])
