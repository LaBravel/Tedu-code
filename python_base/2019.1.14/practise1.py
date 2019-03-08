def myadd(x,y) :
    return x + y
def mysub(x,y) :
    return x - y 
def mymul(x,y) :
    return x * y 
def mydiv(x,y) :
    return x / y
def get_function(s) :
    if s == '加' or s == '+' :
        return myadd
    elif s == '减' or s == '-' :
        return mysub
    elif s == '乘' or s == '*' :
        return mymul
    elif s == '除' or s == '/' :
        return mydiv
while 1 :
    s = input('输入计算公式')
    L = s.split()        
    a = int(L[0])
    b = int(L[2])
    fn = get_function(L[1])
    print('结果是',fn(a,b))

