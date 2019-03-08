try:
    conn = pymysql.connect(host,user,passwd,dbname)
    cursor = conn.cursor()
    sql = '''update acct set balance = balance - 100 where acct = 2131231212'''
    cursor.execute(sql)
    conn.commit()#提交事务
    cursor.close()
    print('插入成功')
except Exception as e :
    conn.rollback()#出现异常，回滚事务
    print('数据库操作失败')
    print(e)
finally :
    conn.close()
