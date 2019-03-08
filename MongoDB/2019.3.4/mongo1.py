from pymongo import *
coon = MongoClient('localhost',27017)
db = coon.test
myset = db.class0

#聚合操作
l = [
    {'$group':{'_id':'$age','num':{'$sum':1}}}
]
cursor = myset.aggregate(l)
for i in cursor :
    print(i)
coon.close()