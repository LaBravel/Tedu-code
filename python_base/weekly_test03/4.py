def turn_title(i) :
    return i.title()

L = []
while 1 :
    a = input('输入一个英文名字,按回车停止')
    if a == '' :
        break
    L.append(a)
L = [i for i in map(turn_title,L)]
print(L)