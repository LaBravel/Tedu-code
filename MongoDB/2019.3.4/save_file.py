'''
将图片以二进制格式存入MongoDB中
'''

from pymongo import mongo_client
import bson.binary

conn = mongo_client('localhost',27017)
db = coon.test
myset = db.class0

#读取图片
with open('mongo.jpg',rb) as f :
    data = f.read()

#做格式转化
content = bson.binary.Binary(data)

#插入数据库
myset.insert_one('filename':'a1.jpg','data':content)

conn.close()