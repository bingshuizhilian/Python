#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' course name：进程和线程 '

__author__ = 'bingshuizhilian'



'''
对于操作系统来说，一个任务就是一个进程（Process），在一个进程内部，要同时干多件事，就需要
同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。

由于每个进程至少要干一件事，所以，一个进程至少有一个线程。当然，像Word这种复杂的进程可以有
多个线程，多个线程可以同时执行，多线程的执行方式和多进程是一样的，也是由操作系统在多个线程
之间快速切换，让每个线程都短暂地交替运行，看起来就像同时执行一样。当然，真正地同时执行多线程
需要多核CPU才可能实现。

多任务的实现有3种方式：多进程模式；多线程模式；多进程+多线程模式。

线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序
自己不能决定什么时候执行，执行多长时间。
'''
### 1.多进程
'''
在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。
'''
print('#'*10, '1.多进程', 'start' if 1 else 'end', '#'*10)

'''multiprocessing'''
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台
# 版本的多进程模块。multiprocessing模块提供了一个Process类来代表一个进程对象。
import os
from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target = run_proc, args = ('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

'''pool'''
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程。
from multiprocessing import Pool
import time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, end - start))

# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
# 调用close()之后就不能继续添加新的Process了。请注意输出的结果，task 0，1，2，3是立刻
# 执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小是CPU的核数。

# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args = (i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

'''子进程'''
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
# 如果子进程还需要输入，则可以通过communicate()方法输入。下面的代码相当于在命令行执行命令nslookup，
# 然后手动输入communicate中的内容。
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)

'''进程间通信'''
'''
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装
了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork
调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进
程去，所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
'''
# 下面的代码以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
from multiprocessing import Queue

# 写数据进程执行的代码
def write_proc(q):
    print('Process to write: %s' % os.getpid())
    for v in ['A', 'B', 'C']:
        print('Put %s to queue...' % v)
        q.put(v)
        time.sleep(random.random())

# 读数据进程执行的代码
def read_proc(q):
    print('Process to read: %s' % os.getpid())
    while True:
        v = q.get(True)
        print('Get %s from queue.' % v)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write_proc, args=(q,))
    pr = Process(target=read_proc, args=(q,))
    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pr，读取
    pr.start()
    # 主进程发送一条消息
    q.put('\'main process send a message\'')
    # 等待pw结束
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()

print('#'*10, '1.多进程', 'start' if 0 else 'end', '#'*10)
