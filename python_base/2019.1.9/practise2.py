a = input("输入一串文字")
d = {}
for i in a :
    if i not in d :
        d.update({i:1})
    else :
        d[i] += 1
for y in range(len(d)) :
    for x in d.keys() :
        if d[x] == max(d.values()) :
            print("字符",x,":",d[x],"次")
            del d[x]