L = []
j = 0
while 1 :
    a = input("输入多行文字")
    if a == '' :
        print("您输入的内容是：")
        break
    L += [a]
    j += len(a)
for i in L :
    print(i)
print("共输入了",len(L),"行文字")
print("共输入了",j,"个字符")
    
