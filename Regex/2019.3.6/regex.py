import re
pattern = r'(\w+):(\d+)'
s = 'zhang:1994 li:1993'

l = re.findall(pattern,s)
print(l)

l = re.split(r'\s+','Hello world ni hao  china')
print(l)

s = re.subn(r'垃圾','**','xxx垃圾,yyy垃圾,qqq垃圾',2)
print(s)