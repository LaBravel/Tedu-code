def sum3(a,b,c) :
    return a + b + c
def pow3(x) :
    return x ** 3
a = float(input('输入一个数：'))
b = float(input('输入一个数：'))
c = float(input('输入一个数：'))
print('3个数立方的和为：',sum3(pow3(a),pow3(b),pow3(c)))
print('3个数和的立方为：',pow3(sum3(a,b,c)))