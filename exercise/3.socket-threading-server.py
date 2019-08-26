#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：3.socket-threading-server '

__author__ = 'bingshuizhilian'



# 仅支持一个客户端，收发消息不阻塞

import socket, threading, datetime

pcname = socket.getfqdn(socket.gethostname())
ip_addr = socket.gethostbyname(pcname)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip_addr, 9999))
s.listen(2)
print('等待用户连接中...')
sock, addr = s.accept()
if sock is not None:
    print('用户%s:%d已连接!!!' % (sock.getsockname()[0], sock.getsockname()[1]))

keepFlag = True

def rec(sk):
    global keepFlag
    while keepFlag:
        t = sk.recv(1024).decode('utf-8')
        if 'exit' == t:
           keepFlag = False
        print('%s:%d' % (sk.getsockname()[0], sk.getsockname()[1]) + datetime.datetime.now().strftime('@%Y%m%d-%H:%M:%S >> ')+ t)

trd = threading.Thread(target=rec, args=(sock,))
trd.start()

while keepFlag:
    t = input()
    sock.send(t.encode('utf-8'))
    if 'exit' == t:
           keepFlag = False

s.close()
