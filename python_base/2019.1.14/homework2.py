def myfac(n) :
    x = 1
    for i in range(1,n + 1) :
        x *= i
    return x
print('前n项积为',myfac(int(input('输入一个正整数'))))