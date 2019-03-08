goods = [
        {'name':'电脑','price':1999},
        {'name':'鼠标','price':10},
        {'name':'游艇','price':20},
        {'name':'美女','price':998},
        ]
a = float(input('输入总资产'))
cost = 0
while 1 :
    for i in goods :
        print(i)
    x = int(input('输入商品序号'))
    cost += goods[x - 1]['price']
    if cost > a :
        print('余额不足！')
        break
    else :
        print('购买成功!')
        x -= cost
