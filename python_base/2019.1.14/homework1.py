def mysum(n) :
    x = 0 
    for i in range(1,n + 1) :
        x += i
    return x
print('前n项和为',mysum(int(input('输入一个正整数'))))