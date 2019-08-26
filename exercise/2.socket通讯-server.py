#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：2.socket通讯-server '

__author__ = 'bingshuizhilian'



# 仅支持一个客户端，收发消息阻塞

import socket

# 待bind的ip/port
ip_port = ('192.168.1.77', 9999)
# 建立socket
s = socket.socket()
# 绑定ip/port
s.bind(ip_port)
# 监听连接
s.listen()
print('等待用户连接中... ...')
while(True):
    #建立连接后，将accept()返回的元组赋值给conn, addr
    conn, addr = s.accept()
    if conn is not None:
        print('有一个用户已连接.\n等待对方发送信息.')
        while(True):
            try:
                recv_data = conn.recv(1024)
                # 现实接收的信息
                print('对方发送的信息：', str(recv_data, encoding='utf-8'))
                send_data = input('给对方发送信息：').strip()
                conn.send(bytes(send_data, encoding='utf-8'))
                print('等待对方回复信息... ...')
            except Exception:
                print('远程主机强迫关闭了一个现有的连接，续继等待其它的连接。')
                break
    conn.close()
