import sys
sys.stdout.write('hello world\n')
f = open('myprint.txt','w')
print('hello world',file = f)