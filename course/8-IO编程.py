#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' course name：IO编程 '

__author__ = 'bingshuizhilian'



### 1.文件读写
# 在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
print('#'*10, '1.文件读写', 'start' if 1 else 'end', '#'*10)

'''读文件'''
# Python内置的open()函数，如果文件打开成功，接下来，调用read()方法可以一次读取
# 文件的全部内容，Python把内容读到内存，用一个str对象表示
f = open('0-连接.py', 'r', encoding = 'utf-8')
print(f.read())
print('f read complete')
f.close()
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，
# 为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现
try:
    f2 = open('0-连接.py', 'r', encoding = 'utf-8')
    print(f2.read())
    print('f2 read complete')
finally:
    if f2:
        f2.close()
# Python引入的with语句可以自动调用close()方法，实际是文件操作类实现了with的接口
with open('0-连接.py', 'r', encoding = 'utf-8') as f3:
    print(f3.read())
    print('f3 read complete')
'''
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，
可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可
以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需
要决定怎么调用。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较
保险；如果是配置文件，调用readlines()最方便。
'''
with open('0-连接.py', 'r', encoding = 'utf-8') as f4, open('0-连接.py', 'r', encoding = 'utf-8') as f5:
    print(f4.readline())
    print('f4 read complete')
    for line in f5.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
    print('f5 read complete')

'''使自定义类型支持with语句'''
'''
with原理 
1.紧跟with后面的语句被求值后，返回对象的“__enter__()”方法被调用，这个方法的返回值
  将被赋值给as后面的变量； 
2.当with后面的代码块全部被执行完之后，将调用前面返回对象的“__exit__()”方法。
'''
class WithTestClass(object):
    def __init__(self, info):
        self.__info = info
    def __enter__(self):
        print('执行了 __enter__方法')
        return self
    def __exit__(self, _type, _value, _trace):
        print('执行了 __exit__方法')
        print("type:", _type)
        print("value:", _value)
        print("trace:", _trace)
    def foo(self):
        print(self.__info)
    def foo2(self):
        bar = 1 / 1 # 1 / 0
        return bar + 10

with WithTestClass('param in') as obj:
    obj.foo()
    print('...delimeter...')
    print(obj.foo2())

'''file-like Object'''
'''
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除
了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定
类继承，只要写个read()方法就行。

StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
'''

'''二进制文件'''
# 前面所述默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、
# 视频等等，用'rb'模式打开文件即可。
with open('0-连接.py', 'rb') as f6:
    print(f6.readline())
    print('f6 read complete')

'''字符编码'''
'''
要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，如open('gbk.txt', 'r', encoding='gbk')
遇到有些编码不规范的文件，可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。

遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
open('gbk.txt', 'r', encoding='gbk', errors='ignore')
'''

'''写文件'''
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件。
import os
with open('testfile.txt', 'w', encoding = 'utf-8') as f7, open('testfile2.txt', 'wb') as f8:
    f7.write('Hello world!')
    f8.write(b'#!/usr/bin/env python3\n')
    print('f7 f8 write complete')
os.remove('testfile.txt') # 这两句删除测试文件，若查看write效果，需要去除此两句的注释
os.remove('testfile2.txt')
'''
可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻
把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有
写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用
with语句来得保险。

要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。以'w'模式写入文件
时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入
'a'以追加（append）模式写入。

所有模式的定义及含义可以参考Python的官方文档https://docs.python.org/3/library/functions.html#open。
'''
print('#'*10, '1.文件读写', 'start' if 0 else 'end', '#'*10)



### 2.StringIO和BytesIO
print('#'*10, '2.StringIO和BytesIO', 'start' if 1 else 'end', '#'*10)



print('#'*10, '2.StringIO和BytesIO', 'start' if 0 else 'end', '#'*10)


