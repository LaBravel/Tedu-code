from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)
#创建数据库对象
db = conn.test
#数据操作
myset = db.class4
# myset.insert_many([
#     {'name':'bbb','num':'12312'},
#     {'name':'ccc','num':'23123'},
#     {'name':'ddd','num':'31213'}
# ])
# myset.save({'name':'bbb','num':'66666','_id':1})

# cursor = myset.find({'name':{'$exists':True}},{'_id':0})
# for i in cursor.limit(3).sort() :
#     print(i)

# dic = {'$or':[{'name':'bbb'},{'name':'aaa'}]}
# d = myset.find_one(dic)
# print(d)


#关闭连接
conn.close()