from socket import *
import struct

ADDR = ('127.0.0.1',1024)
s = socket(AF_INET,SOCK_DGRAM)
while True :
    idno = int(input('id:'))
    name = input('name:')
    height = float(input('height:'))

    fmt = 'i16sf'
    data = struct.pack(fmt,idno,name.encode(),height)
    s.sendto(data,ADDR)

s.close()