import re
pattern = r'\d+'
s = '2019年4月28日'
it = re.finditer(pattern,s)
for i in it :    
    print(i.group())

try :
    obj = re.fullmatch(r'\w+','hello#1973')
    print(obj.group())
except AttributeError :
    pass

obj = re.match(r'[A-Z]\w+','HEllo World')
print(obj.group())

obj = re.search(r'\d+',s)
print(obj.group())