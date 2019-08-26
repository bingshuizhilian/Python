#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：2.socket通讯-client '

__author__ = 'bingshuizhilian'



# 仅支持一个客户端，收发消息阻塞

import socket

#待建立连接HOST的ip/port
ip_port = ('192.168.1.77', 9999)
#建立socket
s = socket.socket()
#建立连接
s.connect(ip_port)
while(True):
    #待发送的信息
    send_data = input('给对方发送信息：').strip()
    s.send(bytes(send_data, encoding='utf-8'))
    print('等待对方回复... ...')
    #接收信息并显示
    recv_data = s.recv(1024)
    print('你有新的消息:', str(recv_data, encoding='utf-8'))
s.close()
