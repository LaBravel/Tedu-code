import os
from time import sleep

a=1
print('====================')
pid = os.fork()

if pid < 0 :
    print('Create process failed')
elif pid == 0 :
    print('Child process')
    print('a=%d' % a)
else :
    sleep(1)
    print('Parent process')
    print('a:%d' % a)