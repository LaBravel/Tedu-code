def mypfh(n) :
    x = 0
    for i in range(1,n + 1) :
        x += i ** 2
    return x
print('前n项平方和为',mypfh(int(input('输入一个正整数'))))