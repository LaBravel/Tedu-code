import re,sys

port = sys.argv[1]

f = open('1.txt','r')
l = f.read()

pattern1 = '%s\\S+' % port
PORT = re.finditer(pattern1,l)


pattern2 = r'Internet address is \S+'
