from socket import *

#创建套接字对象
s = socket()
print(s.family,s.type)
print(s.getsockname())