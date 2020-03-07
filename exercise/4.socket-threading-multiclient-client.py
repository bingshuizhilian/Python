#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：4.socket-threading-multiclient-client '

__author__ = 'bingshuizhilian@yeah.net'



# 收发消息不阻塞

import socket, os
from threading import Thread
from datetime import datetime

class ChatClient(object):
    def __init__(self, address):
        self._socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象，连接服务器
        self._socketClient.connect(address)
        self._keepConnect = True

    def recv_message_handler(self, client):
        while self._keepConnect:
            msg = client.recv(1024).decode('utf-8')
            if 'exit' == msg:
                self._keepConnect = False
                print('服务器离线了，按任意键退出...')
                break
            elif 'cls' == msg:
                os.system("cls")
                msg = '道路千万条，安全第一条'

            print('%s:%d' % (client.getsockname()[0], client.getsockname()[1]) + datetime.now().strftime('@%Y%m%d-%H:%M:%S >> ') + msg)

    def run(self):
        # 开独立线程接收服务器消息
        t = Thread(target=self.recv_message_handler, args=(self._socketClient,))
        t.setDaemon(True)
        t.start()
        # 主线程向服务器发送消息
        while self._keepConnect:
            try:
                msg = input()
                if msg == 'cs':
                    os.system('cls')
                    continue
                self._socketClient.send(msg.encode('utf-8'))
                if 'exit' == msg:
                    self._keepConnect = False
            except Exception as e:
                print('client error occured:', e)

        self._socketClient.close()
        exit()

if __name__ == "__main__":
    ip_addr = input('输入服务端IP地址([1]：默认IP、[2]：本机IP、[其他]：自定义IP)：').strip()
    if '1' == ip_addr:
        ip_addr = '192.168.0.101'
    elif '2' == ip_addr:
        pcname = socket.getfqdn(socket.gethostname())
        ip_addr = socket.gethostbyname(pcname)

    ADDRESS = (ip_addr, 9999)  # 绑定地址
    
    cc = ChatClient(ADDRESS)
    cc.run()