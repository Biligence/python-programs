# coding: utf-8 
""" 
ping一个网段，并列出结果 
""" 
 
import os, re, threading 
 
RESULT_PATTERN = re.compile(r'Lost\s=\s(\d)', re.M) 
 
class Ping(threading.Thread): 
    def __init__(self, ip_address): 
        threading.Thread.__init__(self) 
        self.ip_address = ip_address 
 
    def run(self): 
        # ping 指定的IP地址，并返回丢失的包数 
        result = os.popen('ping -n 4 %s' % self.ip_address).read() 
        match = RESULT_PATTERN.search(result) 
        lost_count = match and int(match.group(1)) or 0 
 
        # 加锁以防止屏幕打印混乱 
        global lock 
        lock.acquire() 
        if lost_count == 0: 
            print 'ping %-15s      stabled' % self.ip_address 
        elif lost_count == 4: 
            print 'ping %-15s      timeout' % self.ip_address 
        else: 
            print 'ping %-15s      unstable' % self.ip_address 
        lock.release() 
 
def bulk_ping(ip_prefix, start=0, end=255): 
    print 'pinging ip addresses from %s.%d to %s.%d' % (ip_prefix, start, ip_prefix, end) 
    for i in range(start, end): 
        ping_thread = Ping('%s.%d' % (ip_prefix, i)) 
        ping_thread.start() 
 
if __name__ == '__main__': 
    global lock 
    lock = threading.Lock() 
    bulk_ping('192.168.6')