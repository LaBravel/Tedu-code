import pymysql
host = 'localhost'#服务器地址
user = 'root'#用户名
passwd = '123456'#密码
dbname = 'mysql'#库名称
conn = pymysql.connect(host,user,passwd,dbname)#建立数据库连接
cursor = conn.cursor()#获取游标对象
cursor.execute('select * from acct')#传入需执行的mysql语句
result = cursor.fetchall()#获取查询结果
for r in result :#遍历结果集并打印
    tmp = '帐号：%s,姓名：%s,余额：%s,%s,%s,%s,%s' % (r[0],r[1],r[2],
    r[3],r[4],r[5],r[6])
    print(tmp)
cursor.close()#关闭游标对象
conn.close()#关闭数据库连接
print('查询完成')