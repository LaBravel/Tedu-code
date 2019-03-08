x = input('输入一串字符')
y = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
j = 0
k = 0 
for i in x :
    if i == ' ' :
        j += 1
else :
    print('有',j,'个空格')

for i in x :
    if i in y :
        k += 1
else :
    print('有',k,'个英文字母') 

