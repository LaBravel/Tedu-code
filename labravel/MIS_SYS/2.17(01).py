#l=['中国人民解放军','社交直觉','废物测试','c']
#d={i:len(i) for i in l}
#print(d)
#d={x:x**2 for x in range(10)}
#print(d)
#for i in l:                                                                                                                     
#d={i:len(i)}
s1={'曹操','刘备','孙权'}
#s2={'关羽','张飞'，'孙权'}
s2={'曹操','张飞','关羽','孙权'}
s3=s1&s2
print(s3)
s4=s1-s2
print(s4)
s5=s2-s1
print(s5)
s6=s1^s2
print(s6)
s7=s1|s2
print('经理及技术人员分别是:',s7)
print('经理及技术人员一共有',len(s7),'人')
if '张飞' in s1:
    print('张飞是经理')
else:
    print('张飞不是经理')