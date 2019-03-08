f = open('mynote.txt','a')
f.write('ABCD\n')
f.write('你好\n')
f.writelines(['abcd\n','1234\n'])
f.close