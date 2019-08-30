#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：4.socket-threading-multiclient-server '

__author__ = 'bingshuizhilian@yeah.net'



# 支持多客户端，收发不阻塞

'''
参考：https://blog.csdn.net/qq_39687901/article/details/81531101

首先，需要明白的是socket的accept和recv这两个方法是阻塞线程的。这就意味着我们需要新开线程来处理这两个方法。
具体的程序流程大概是这样的：
1.新开一个线程用于接收新的连接（socket.accept()）
2.当有新的连接时，再新开一个线程，用于接收这个连接的消息（socket.recv()）
3.主线程做为控制台，接收用户的输入，进行其他操作
也就是说，服务端需要为每一个连接创建一个线程。
'''

import socket
from threading import Thread
from datetime import datetime

class ChatServer(object):
    def __init__(self, address):
        self._socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象，负责监听的socket
        self._socketServer.bind(address)
        self._socketServer.listen(5)  # 最大等待数（有很多人理解为最大连接数，其实是错误的）
        self._connectPool = []  # 连接池
        print("服务端已启动，等待客户端连接...")

    def accept_client(self):
        # 接收新连接
        while True:
            client, address = self._socketServer.accept()  # 阻塞，等待客户端连接
            self._connectPool.append(client)  # 加入连接池
            print("客户端{}上线了。".format(address))
            # 开独立线程接收客户端消息
            t = Thread(target=self.recv_message_handler, args=(client, address))  # 给每个客户端创建一个独立的线程进行管理
            t.setDaemon(True)  # 设置成守护线程
            t.start()

    def recv_message_handler(self, client, address):
        # 消息处理
        client.sendall("连接服务器成功!".encode(encoding='utf8'))
        while True:
            recBytes = client.recv(1024).decode('utf-8')
            if len(recBytes) == 0 or 'exit' == recBytes:
                client.close()
                self._connectPool.remove(client)
                print("客户端{}下线了。".format(address))
                break
            print('%s:%d' % (address[0], address[1]) + datetime.now().strftime('@%Y%m%d-%H:%M:%S >> ')+ recBytes)

    def run(self):
        # 开独立线程处理多客户端连接
        t = Thread(target=self.accept_client)  # 新开一个线程，用于接收新连接
        t.setDaemon(True)
        t.start()
        # 主线程向客户端发送消息
        while True:
            cmd = input('--------------------------\n'
                        '输入1:查看当前在线人数\n'
                        '输入2:给指定客户端发送消息\n'
                        '输入3:广播消息\n'
                        '输入4:关闭服务端\n')
            if '1' == cmd:
                print("--------------------------")
                print("当前在线人数：", len(self._connectPool))
            elif '2' == cmd:
                print("--------------------------")
                index, msg = input("请输入“索引 消息”的形式：").split(' ')
                if int(index) < len(self._connectPool):
                    self._connectPool[int(index)].sendall(msg.encode(encoding='utf-8'))
                else:
                    print('索引%d不存在' % int(index))
            elif '3' == cmd:
                print("--------------------------")
                msg = input("请输入广播消息：")
                for i in range(len(self._connectPool)):
                    self._connectPool[i].sendall(msg.encode(encoding='utf-8'))
            else:
                for i in range(len(self._connectPool)):
                    self._connectPool[i].sendall('exit'.encode(encoding='utf-8'))
                exit()
        
        self._socketServer.close()
        exit()

if __name__ == "__main__":
    pcname = socket.getfqdn(socket.gethostname())
    ip_addr = socket.gethostbyname(pcname)
    ADDRESS = (ip_addr, 9999)  # 绑定地址
    
    cs = ChatServer(ADDRESS)
    cs.run()
