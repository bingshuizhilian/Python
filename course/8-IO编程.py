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
    f6_readline = f6.readline()
    print(f6_readline)
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
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
print('#'*10, '2.StringIO和BytesIO', 'start' if 1 else 'end', '#'*10)

from io import StringIO
f9 = StringIO()
f9.write('hello world')
f9.write('\nhello world2')
print(f9.getvalue()) # getvalue()方法用于获得写入后的str

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
f10 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f10.readline()
    if s == '':
        break
    print(s.strip())

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO，BytesIO实现了在内存中读写bytes。
from io import BytesIO

f11 = BytesIO()
f11.write('中华人民共和国'.encode('utf-8'))
f11.write(b'welcome')
print(f11.getvalue())

# 注意，写入的不是str，而是经过UTF-8编码的bytes。和StringIO类似，可以用一个bytes初始化BytesIO，然后，
# 像读文件一样读取即可。
f12 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f12.read())
print(f12.getvalue())
print(f12.getbuffer())

print('#'*10, '2.StringIO和BytesIO', 'start' if 0 else 'end', '#'*10)



### 3.操作文件和目录
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。
print('#'*10, '3.操作文件和目录', 'start' if 1 else 'end', '#'*10)

import os

print(os.name)
print(os.environ)
print(os.environ.get('PATH'), '\n', os.environ.get('PATH') == os.getenv('PATH'))

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，查看、创建和删除目录示例如下。
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
testdir = os.path.join(os.path.abspath('.'), 'testdir')
print(testdir)
# 然后创建一个目录
os.mkdir(testdir)
# 删掉一个目录
os.rmdir(testdir)

r'''
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的
路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：part-1/part-2；而Windows下会返回
这样的字符串：part-1\part-2。

同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分
为两部分，后一部分总是最后级别的目录或文件名。
'''
testdir2, testfilename = os.path.split('e:\\GITHUB\\Python\\course')
print(testdir2)
print(testfilename)

testdir3, testfilename2 = os.path.split('e:\\GITHUB\\Python\\course\\0-连接.py')
print(testdir3)
print(testfilename2)

# os.path.splitext()可以直接得到文件扩展名，很多时候非常方便
testdir4, testfilename3 = os.path.splitext('e:\\GITHUB\\Python\\course\\0-连接.py')
print(testdir4)
print(testfilename3)

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
# 创建文件
with open('testfile.txt', 'w+', encoding = 'utf-8') as f13:
    f13.write('This is a test file.')
# 对文件重命名
os.rename('testfile.txt', 'testfile.py')
# 删除文件
os.remove('testfile.py')
# os模块中不存在复制文件的函数，幸运的是shutil模块提供了copyfile()的函数，还可以
# 在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
import shutil
shutil.copyfile('C:/windows/system.ini', os.path.join(os.path.abspath('.'), 'testfile.ini'))
os.remove('testfile.ini')

# 利用Python的特性来过滤文件
# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

print('#'*10, '3.操作文件和目录', 'start' if 0 else 'end', '#'*10)



### 4.序列化
'''
变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之
为serialization，marshalling，flattening等等，都是一个意思。序列化之后，就可以把序列化后
的内容写入磁盘，或者通过网络传输到别的机器上。反过来，把变量内容从序列化的对象重新读到内存里
称之为反序列化，即unpickling。Python提供了pickle模块来实现序列化。

Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。
但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的
规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
'''
print('#'*10, '4.序列化', 'start' if 1 else 'end', '#'*10)

'''pickle'''
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本
# 的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

# 把一个对象序列化并写入文件
import pickle
dic = dict(name='Bob', age=20, score=88)
print(pickle.dumps(dic))

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另
# 一个方法pickle.dump()直接把对象序列化后写入一个file-like Object。看看写入的dump.txt文件，
# 一堆乱七八糟的内容，这些都是Python保存的对象内部信息。
with open('dump.txt', 'wb') as f14:
    pickle.dump(dic, f14)

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列
# 化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
with open('dump.txt', 'rb') as f15:
    dic2 = pickle.load(f15)
    print(dic2)

os.remove('dump.txt')

'''JSON'''
'''
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序
列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过
网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
'''
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。先把Python对象变成一个JSON。
import json
print(json.dumps(dic))

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个
# file-like Object。要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者
# 把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化。
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

with open('dump2.txt', 'w') as f16:
    json.dump(dic, f16)

with open('dump2.txt', 'r') as f17:
    dic3 = json.load(f17)
    print(type(dic3), dic3)

os.remove('dump2.txt')

'''JSON进阶'''
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义
# Student类，然后序列化。
class StudentJson(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
# dumps()方法的参数列表可以参考文档https://docs.python.org/3/library/json.html#json.dumps
# 这些可选参数就是让我们来定制JSON序列化。只有前面的代码是无法把Student类实例序列化为JSON的，因为
# 默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。可选参数default就是把任意
# 一个对象变成一个可序列为JSON的对象，我们需要为StudentJson专门写一个转换函数，再把函数传进去即可。
def student2dict(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'score': stu.score
    }
# StudentJson实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
stu = StudentJson('Lily', 18, 96)
print(json.dumps(stu, default=student2dict))

'''
不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变
为dict，因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，
比如定义了__slots__的class。
'''
stu2 = StudentJson('David', 21, 85)
print(json.dumps(stu2, default=lambda obj: obj.__dict__))

# 同样的道理，如果我们要把JSON反序列化为一个StudentJson对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为StudentJson实例。
def dict2student(dic):
    return StudentJson(dic['name'], dic['age'], dic['score'])
# 反序列化的Student实例对象
json_str2 = '{"age": 17, "score": 78, "name": "Lilei"}'
stu3 = json.loads(json_str2, object_hook=dict2student)
print(stu3)

# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响
dic4 = dict(name='小明', age=20)
print(json.dumps(dic4, ensure_ascii=True))
print(json.dumps(dic4, ensure_ascii=False))

print('#'*10, '4.序列化', 'start' if 0 else 'end', '#'*10)
