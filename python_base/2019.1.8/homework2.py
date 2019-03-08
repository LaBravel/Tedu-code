L1 = []
L2 = []
L3 = []
while 1 :
    x = input("输入任意整数")
    if x == '' :
        print("L1:",L1,sep = '')
        break
    L1.append(x)
for i in L1 :
    if i not in L2 :
        L2.append(i)
for i in L2 :
    L1.remove(i)
for i in L1 :
    if i not in L3 :
        L3.append(i)
print("L2:",L2,'\n',"L3:",L3,sep = '')