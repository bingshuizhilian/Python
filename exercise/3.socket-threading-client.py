#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：3.socket-threading-client '

__author__ = 'bingshuizhilian'



# 仅支持一个客户端，收发消息不阻塞

import socket, threading, datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_addr = input('输入服务端IP地址([1]：默认IP、[2]：本机IP、[其他]：自定义IP)：').strip()

if '1' == ip_addr:
    ip_addr = '192.168.1.77'
elif '2' == ip_addr:
    pcname = socket.getfqdn(socket.gethostname())
    ip_addr = socket.gethostbyname(pcname)

s.connect((ip_addr, 9999))

keepFlag = True

def rec(sock):
    global keepFlag
    while keepFlag:
        t = sock.recv(1024).decode('utf-8')
        if 'exit' == t:
           keepFlag = False
        print('%s:%d' % (sock.getsockname()[0], sock.getsockname()[1]) + datetime.datetime.now().strftime('@%Y%m%d-%H:%M:%S >> ')+ t)

trd = threading.Thread(target=rec, args=(s,))
trd.start()

while keepFlag:
    t = input()
    s.send(t.encode('utf-8'))
    if 'exit' == t:
           keepFlag = False

s.close()
