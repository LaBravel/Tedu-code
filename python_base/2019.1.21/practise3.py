def myeven(begin,end) :
    i = begin
    while i < end :
        if i % 2 == 0 :
            yield i
        i += 1

a = int(input('输入开始数'))
b = int(input('输入结尾数'))
for j in myeven(a,b) :
    print(j)
print([k ** 2 for k in myeven(a,b) ])