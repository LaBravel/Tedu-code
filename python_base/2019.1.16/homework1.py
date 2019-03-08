def fun(i) :
    from math import factorial as fac
    if i == 0 : 
        return 1
    return (1 / fac(i)) + fun(i - 1)

print(fun(int(input('输入一个正整数'))))
    