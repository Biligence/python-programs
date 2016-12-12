import socket
input=open('F:\\jj\\GIS\\Scirpts\\Python Scripts\\ip.txt')
output=open('F:\\jj\\GIS\\Scirpts\\Python Scripts\\hostname.txt','w')
buffer=''
for line in input:
    try:
        line=line[:-1]
        hostname=socket.gethostbyaddr(line)
        buffer=buffer+hostname[0]+'\n'
    except:
        buffer=buffer+'\n'
input.close() 
output.write(buffer)
output.close()


