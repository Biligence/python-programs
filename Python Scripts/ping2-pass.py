
import re
from subprocess import Popen, PIPE
from threading import Thread


class Pinger(object):
    def __init__(self, hosts):
        for host in hosts:
            pa = PingAgent(host)
            pa.start()
        
class PingAgent(Thread):
    def __init__(self, host):
        Thread.__init__(self)        
        self.host = host

    def run(self):
        p = Popen('ping -n 1 ' + self.host, stdout=PIPE)
        m = re.search(r'Average = (\d*)ms', str(p.stdout.read()))
        if m: print('Round Trip Time: %s ms -' % m.group(1), self.host)
        else: print('Error: Invalid Response -', self.host)
              
                             
if __name__ == '__main__':
    hosts = [
        'www.pylot.org',
        'www.goldb.org',
        'www.google.com',
        'www.this_one_wont_work.com',
        'xxxtest.com'
       ]
    Pinger(hosts)
