#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' course name：进程和线程，本节为子章节，内容为分布式进程中的task_master部分 '

__author__ = 'bingshuizhilian'



# 服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务
import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 定义回调函数
def get_task():
    return task_queue

def get_result():
    return result_queue

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

def test():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象
    # QueueManager.register('get_task_queue', callable=lambda: task_queue) # windows下绑定调用接口不能使用lambda
    # QueueManager.register('get_result_queue', callable=lambda: result_queue)
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)

    # 绑定端口5000, 设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc') # windows下需要填写ip地址，linux下不填默认为本地
    # 启动Queue
    manager.start()
    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=60)
        print('Result: %s' % r)
    # 关闭
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    #windows下多进程可能会炸，添加这句可以缓解
    freeze_support()
    test()