a = input("请输入第一句文字")
b = input("请输入第二句文字")
c = input("请输入第三句文字")
width = max(len(a),len(b),len(c)) + 2
a1 = a.replace(' ','')
b1 = b.replace(' ','')
c1 = c.replace(' ','')
print('+','-' * width,'+')
print('|',a1.center(width),'|')
print('|',b1.center(width),'|')
print('|',c1.center(width),'|')
print('+','-' * width,'+')