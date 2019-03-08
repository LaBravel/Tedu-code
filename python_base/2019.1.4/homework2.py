#第一问
i = 65 
while i <= 90 :
    print(chr(i),end = '')
    i += 1
else :
    i = 65
    print('')

#第二问
while i <= 90 :
    print(chr(i),chr(i + 32),sep = '',end = '')
    i += 1
else :
    print('')