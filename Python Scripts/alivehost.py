import subprocess
from subprocess import *
import re

input=open('C:\\jzhouja\\GIS\\Scirpts\\Python Scripts\\hosts.txt')
output=open('C:\\jzhouja\\GIS\\Scirpts\\Python Scripts\\alive.txt','w')
buffer=''
for host in input:
        host=host[:-1]
        pingcmd="ping -n %i %s" % (1,host )
        execute=subprocess.Popen(pingcmd,stdout=PIPE)
        result=str(execute.communicate()[0])
        m=re.search('Reply from',result)
        if m: buffer=buffer+host+' y\n'
        else: buffer=buffer+host+' N\n'
input.close() 
output.write(buffer)
output.close()
