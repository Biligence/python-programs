import socket
test=open('C:\\jzhouja\\GIS\\Scirpts\\hostname.txt')
output=open('C:\\jzhouja\\GIS\\Scirpts\\ip.txt','w')
buffer=''
for line in test:
    try:
        line=line[:-1]
        ip=socket.gethostbyname(line)
        buffer=buffer+ip+'\n'
    except:
        buffer=buffer+'\n'
test.close() 
output.write(buffer)
output.close()


