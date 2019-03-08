begin = int(input("从哪个数开始？"))
end = int(input("到哪个数为止？"))
x = 1
while begin < end :
    if x % 5 != 0 :
        print(begin,end = ' ')
        begin += 1
        x += 1
    else :
        print(begin,end = '\n')
        begin += 1
        x += 1 
else :
    print('\n',"程序结束") 