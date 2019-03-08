from db_oper import *
from acct_manage import *

if __name__ == '__main__' :
    db_oper = DBOper('localhost','root','123456','mysql')
    db_oper.open_conn() 
    am = AcctManage(db_oper)
    menu = '''
    ----------请选取要执行的操作-----------
    1-查询所有
    2-根据账户查询
    '''
    print(menu)
    oper = input('请选取要执行的操作')
    if oper == '1' :
        accts = am.query_all_acct()
        for acct in accts :
            print(acct)
    if oper == '2' :
        acct_no = input('请输入要查询的帐号')
        acct = am.query_by_id(acct_no)
        print(acct)
    else :
        print('选取的操作暂不支持')