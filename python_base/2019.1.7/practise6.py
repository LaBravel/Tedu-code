x = 0
for i in range(1,101) :
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or \
       i % 7 == 0 :
        continue
    x += i
print(x)