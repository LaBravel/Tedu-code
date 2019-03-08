import re

s1 = 'Welcome to 北京'
s2 = 'Welcome to \n北京'
s3 = '''Welcome to 
北京'''

regex1 = re.compile(r'\w+')
regex2 = re.compile(r'\w+',flags=re.A) #只匹配ACSII字符
regex3 = re.compile(r'[a-z]+',flags=re.I) #忽略字母大小写
regex4 = re.compile(r'.+',flags=re.S) #让'.'能够匹配换行符
regex5 = re.compile(r'^北京$',flags=re.M) #变得能够匹配每一行的始末为止
regex6 = re.compile(r'''[A-Z][a-z]* #匹配第一个单词
    \s+\w+ #匹配第二个单词
    \s+\w+''', #匹配第三个单词
    flags=re.X) #变得能够添加注释
l1 = regex1.findall(s1)
l2 = regex2.findall(s1)
l3 = regex3.findall(s1)
l4 = regex4.findall(s2)
l5 = regex5.findall(s3)
l6 = regex6.findall(s1)
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)