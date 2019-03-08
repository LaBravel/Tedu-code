f = open('char20.txt','wb')
b = b'ABCD1234abcd6666'
f.write(b)
f = open('char20.txt','rb')
print('当前文件的读写位置是',f.tell())
b = f.read(3)
print('b=',b)
print('读过３个字节后的读写位置是',f.tell())

