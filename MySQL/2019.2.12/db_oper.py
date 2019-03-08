import pymysql
class DBOper :
    def __init__(self,host,user,passwd,dbname) :
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.conn = None
        self.cursor = None

    def open_conn(self) :
        self.conn = pymysql.connect(
                    self.host,
                    self.user,
                    self.passwd,
                    self.dbname)
        self.cursor = self.conn.cursor()
        print('连接数据库成功')
        
    def close_conn(self) :
        self.conn.close()
        print('数据库关闭')
    
    def do_query(self,sql) :
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # for r in result :#遍历结果集并打印
        #     tmp = '帐号：%s,姓名：%s,余额：%s,%s,%s,%s,%s' % (r[0],r[1],r[2],
        #         r[3],r[4],r[5],r[6])
        #     print(tmp)    
        print('查询成功')
        return result
    
    def do_update(self,sql) :
        self.cursor.execute(sql)
        self.conn.commit()#提交事务
        print('执行成功,修改笔数为%d' % self.cursor.rowcount)
