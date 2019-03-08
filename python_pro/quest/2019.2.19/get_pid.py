import os
from time import sleep

pid = os.fork()

if pid < 0 :
    print('Create process failed')
elif pid == 0 :
    sleep(1)
    print('Child pid:',os.getpid())
    print('Get parent pid:',os.getppid())
else :
    print('Parent pid:',os.getpid())
    print('Get Child pid:',pid)
