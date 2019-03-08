f = open('myfile00.bin','wb')#wb为二进制操作
b = bytes(range(256))
print(b)
r = f.write(b)
print('成功写入',r,'个字节')
f.close()