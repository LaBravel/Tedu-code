def myyield() :
    yield 2
    yield 3
    yield 4
    yield 5
    print('myyield函数运行结束')

for i in myyield() :
    print(i)
print('程序正常结束')