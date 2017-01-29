# -*- coding: utf-8 -*-
"""
Created on 2017

@author: WHUER
"""
import StringIO
import pycurl
import sys
import os
import time

class idctest:
    def __init__(self):
          self.contents = ''
    def body_callback(self,buf):
          self.contents = self.contents + buf

def get_bandwidth(input_url):
    t = idctest()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL,input_url)
    c.setopt(pycurl.MAXREDIRS, 5)
    try:
        c.perform()
    except:
        c.perform()


    http_code = c.getinfo(pycurl.HTTP_CODE)
    dns_resolve = c.getinfo(pycurl.NAMELOOKUP_TIME)
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)
    http_pre_trans = c.getinfo(pycurl.PRETRANSFER_TIME)
    http_start_trans = c.getinfo(pycurl.STARTTRANSFER_TIME)
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)
    http_size_download = c.getinfo(pycurl.SIZE_DOWNLOAD)
    http_header_size = c.getinfo(pycurl.HEADER_SIZE)
    http_speed_downlaod = c.getinfo(pycurl.SPEED_DOWNLOAD)
    bandwidth = http_speed_downlaod/1024/1024*8
    return bandwidth

if __name__ == '__main__':
   input_url = 'http://211.137.51.152/cache/sw.bos.baidu.com/sw-search-sp/software/9e85b452bf53e/Baidu_Setup_5388_3.2.0.3068_10000009.exe?ich_args2=100-29151407054307_591c84bf8ef8b74eccc6969ac606795d_10068001_9c886c29d1c4f5d19f32518939a83798_7efac374a5b0e2684e57728b470136ba'#sys.argv[1]
   get_bandwidth(input_url)
