import random
l1 = ['红桃' + str(i) for i in range(1,14)]
x = 0 
random.shuffle(l1)
print(l1)
for i in l1 :
    if i == '红桃8' :
        x = l1.index(i)

if x != 0 :
    print('找到了,是第',x,'张')
else:
    print('查询失败')

