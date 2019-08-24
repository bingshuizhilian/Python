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

# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程
#     q = Queue()
#     pw = Process(target=write_proc, args=(q,))
#     pr = Process(target=read_proc, args=(q,))
#     # 启动子进程pw，写入
#     pw.start()
#     # 启动子进程pr，读取
#     pr.start()
#     # 主进程发送一条消息
#     q.put('\'main process send a message\'')
#     # 等待pw结束
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止
#     pr.terminate()

print('#'*10, '1.多进程', 'start' if 0 else 'end', '#'*10)



### 2.多线程
'''
多任务可以由多进程完成，也可以由一个进程内的多线程完成。进程是由若干线程组成的，一个进程至少有一个线程。

线程是操作系统直接支持的执行单元，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是
真正的Posix Thread，而不是模拟出来的线程。

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread
进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。Python解释器由于设计时有
GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
'''
print('#'*10, '2.多线程', 'start' if 1 else 'end', '#'*10)
'''
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模
块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建
时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动
给线程命名为Thread-1，Thread-2···
'''
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
import time, threading
# 新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(0.1)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)

'''lock'''
'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在
于多个线程同时改一个变量，把内容给改乱了。
'''
# 错误使用示例
balance = 0

def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''
究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象
的内容改乱了。两个线程同时一存一取，就可能导致balance不对，所以，我们必须确保一个线程在修改balance的时
候，别的线程一定不能改。

如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该
线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由
于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通
过threading.Lock()来实现的。

当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到
获得锁为止。获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用
try...finally来确保锁一定会被释放。锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当
然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，
由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，
既不能执行，也无法结束，只能靠操作系统强制终止。
'''
balance = 0
lock = threading.Lock()

def run_thread_safe(n):
    for i in range(100000):
        # 先要获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完了一定要释放锁
            lock.release()

t3 = threading.Thread(target=run_thread_safe, args=(5,))
t4 = threading.Thread(target=run_thread_safe, args=(8,))
t3.start()
t4.start()
t3.join()
t4.join()
print(balance)

'''多核CPU'''
# 一个死循环线程会100%占用一个CPU。要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。
import multiprocessing

cpu_counts = multiprocessing.cpu_count()
print(cpu_counts)

def infinate_loop():
    x = 0
    while True:
        x = x ^ 1

# for i in range(cpu_counts):
#     t = threading.Thread(target=infinate_loop)
#     t.start()

'''
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的
线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能
交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除
非重写一个不带GIL的解释器。所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定
要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python
进程有各自独立的GIL锁，互不影响。
'''

print('#'*10, '2.多线程', 'start' if 0 else 'end', '#'*10)



### 3.ThreadLocal
'''
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了
参数在一个线程中各个函数之间互相传递的问题。

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调
用到的处理函数都可以非常方便地访问这些资源。
'''
print('#'*10, '3.ThreadLocal', 'start' if 1 else 'end', '#'*10)
# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    st = local_school.student
    print('Hello, %s (in %s)' % (st, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()

t5 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t6 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t5.start()
t6.start()
t5.join()
t6.join()

print('#'*10, '3.ThreadLocal', 'start' if 0 else 'end', '#'*10)



### 4.进程vs线程
print('#'*10, '4.进程vs线程', 'start' if 1 else 'end', '#'*10)

r'''
(1)进程和线程的对比
首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多
任务环境下，通常是一个Master，多个Worker。如果用多进程实现Master-Worker，主进程就是Master，其他进程就
是Worker。如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有
进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式。

多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。另
外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都
会成问题。

多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造
成整个进程崩溃，因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，经常可以看到这样
的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。在Windows
下，多线程的效率比多进程要高。

(2)线程切换
无论是多进程还是多线程，只要数量一多，效率就会上不去。操作系统在切换进程或者线程时也是一样的，它需要先保存
当前执行的现场环境（CPU寄存器状态、内存页等），然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换
内存页等），才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，操作系统可能
就主要忙着切换任务，根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死
状态。所以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好。

(3)计算密集型 vs. IO密集型
是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型。

计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算
能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就
越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。

计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合
计算密集型任务。对于计算密集型任务，最好用C语言编写。

第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大
部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，
但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。

IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样
运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的
语言，脚本语言是首选，C语言在开发效率上会差很多。

(4)异步IO
考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任
务无法并行执行，因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。

现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，就可以
用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上
采用单进程模型就可以高效地支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由
于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势。

对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。后面的章
节《异步IO》会讨论如何编写协程。
'''

print('#'*10, '4.进程vs线程', 'start' if 0 else 'end', '#'*10)



### 5.分布式进程
# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
print('#'*10, '5.分布式进程', 'start' if 1 else 'end', '#'*10)

print('本节示例需要运行“9-子章节-分布式进程-task_master.py”和“9-子章节-分布式进程-task_worker.py”来查看')

r'''介绍
在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能
分布到同一台机器的多个CPU上。

Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以
作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很
容易地编写分布式多进程程序。
'''

r'''例子
写在前面：
第一点windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定，原因是当一个对象被放入一个队列中时，这个对象
首先会被一个后台线程用pickle序列化，并将序列化后的数据通过一个底层管道的管道传递到队列中，这就是lambda函数不能被
pickled的原因：所有lambda函数都具有相同的名称：<lambda>；
第二点绑定端口并设置验证码，windows下需要填写ip地址，linux下不填默认为本地；
详情可以参考https://blog.kasora.moe/2016/06/12/python-%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/。

举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把
发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？

原有的Queue可以继续使用，并且通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。

我们先看服务进程的源代码：file:///E:/GITHUB/Python/course/9-进程和线程-分布式进程-task_master.py。

请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直
接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。

然后在另一台机器上启动任务进程(本机上启动也可以)：file:///E:/GITHUB/Python/course/9-进程和线程-分布式进程-task_worker.py。

任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。现在，可以试试分布式进程的工作效果了。先启动task_master.py服务
进程，task_master.py进程发送完任务后，开始等待result队列的结果。然后启动task_worker.py进程task_worker.py进程结束，在
task_master.py进程中会继续打印出结果。
'''

r'''例子后话
这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分
布到几台甚至几十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。

Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中。而Queue之
所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起
个名字，比如get_task_queue。

authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果task_worker.py的authkey和task_master.py的authkey
不一致，肯定连接不上。

注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志
文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
'''

print('#'*10, '5.分布式进程', 'start' if 0 else 'end', '#'*10)
