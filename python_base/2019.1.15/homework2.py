def super_print(list) :
    global i
    i = 0
    if type(list) is int :
        L_output.append(list)
        return list
    if list[0] == [] :
        del list[0]
    aaa = super_print(list[0])
    if i == 0 :
        del list[0]
        i += 1    
    return list

L = [[3,5,8],10,[[13,14],15,18],20]
L_output = []
while L != [] :
    super_print(L)
print(L_output)
print('所有数之和为',sum(L_output))

