#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：4.socket-threading-multiclient-server '

__author__ = 'bingshuizhilian@yeah.net'



# 支持多客户端，收发不阻塞

import socket, socketserver
from threading import Thread
from datetime import datetime

class ChatServer(socketserver.BaseRequestHandler):
    def setup(self):
        self.request.sendall("连接服务器成功!".encode(encoding='utf8'))

    def handle(self):
        print("客户端{}上线了。".format(self.client_address))
        # 开独立线程接收客户端消息
        t = Thread(target=self.recvmsg, args=(self.request, self.client_address))  # 给每个客户端创建一个独立的线程进行管理
        t.setDaemon(True)  # 设置成守护线程
        t.start()
        self.sendmsg()

    def recvmsg(self, client, address):
        # 消息处理
        while True:
            recBytes = client.recv(1024).decode('utf-8')
            if len(recBytes) == 0 or 'exit' == recBytes:
                client.close()
                print("客户端{}下线了。".format(address))
                break
            print('%s:%d' % (address[0], address[1]) + datetime.now().strftime('@%Y%m%d-%H:%M:%S >> ')+ recBytes)

    def sendmsg(self):
        # 主线程向客户端发送消息
        while True:
            msg = input()
            self.request.sendall(msg.encode(encoding='utf-8'))


if __name__ == "__main__":
    pcname = socket.getfqdn(socket.gethostname())
    ip_addr = socket.gethostbyname(pcname)
    ADDRESS = (ip_addr, 9999)  # 绑定地址
    
    cs = socketserver.ThreadingTCPServer(ADDRESS, ChatServer)
    cs.serve_forever()