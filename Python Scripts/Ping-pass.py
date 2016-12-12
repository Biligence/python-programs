import subprocess

count = input("Number of times to ping host: ")
co=int(count)
host = input("IP of host to ping: ")
pingcmd = "ping -n %i %s" % (co, host)
execute = subprocess.Popen(pingcmd)
results = execute.readlines()
execute.close()
length = len(results)
for x in range (length) :
    print(results[x])
