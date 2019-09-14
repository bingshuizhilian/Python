#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' course name：常用内建模块 '

__author__ = 'bingshuizhilian@yeah.net'



' Python之所以自称“batteries included”，就是因为内置了许多非常有用的模块，无需额外安装和配置，即可直接使用 '



### 1.datetime
'''
datetime是Python处理日期和时间的标准库，datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地
时间。如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

详细使用可参考https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
'''
print('#'*10, '1.datetime', 'start' if 1 else 'end', '#'*10)
# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类
# 如果仅导入import datetime，则必须引用全名datetime.datetime

from datetime import datetime

# 获取当前日期和时间
now = datetime.now()
print(now, type(now))

# 获取指定日期和时间
dt = datetime(2019, 9, 10, 9, 52)
print(dt)

# datetime转换为timestamp
'''
在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年
以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。

你可以认为：timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00，对应的北京时间是：timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00。
可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是
为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。

注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。本地时间是指
当前操作系统设定的时区。timestamp也可以使用datetime.utcfromtimestamp直接被转换到UTC标准时区的时间。
'''
print(dt.timestamp())
t = 153518688.6
print(datetime.fromtimestamp(t))  # 本地时间（实际上就是UTC+8:00时区的时间）
print(datetime.utcfromtimestamp(t))  # UTC时间（实际上就是UTC+0:00时区的时间）

# str转换为datetime
'''
很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()
实现，需要一个日期和时间的格式化字符串。

下例中字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式，注意转换后的datetime是没有时区信息的。
'''
cday = datetime.strptime('2019-09-10 11:29:30', '%Y-%m-%d %H:%M:%S')
print(cday, type(cday))

# datetime转换为str
'''
如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期
和时间的格式化字符串。
'''
print(now.strftime('%a, %b %d, %H:%M:%S'))

# datetime加减
'''
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta
这个类，使用timedelta可以很容易地算出前几天和后几天的时刻。
'''
from datetime import timedelta
print(now)
print(now + timedelta(hours=10))
print(now + timedelta(hours=-10))
print(now + timedelta(hours=-24) == now - timedelta(days=1))
print(now + timedelta(days=1, hours=-10))
print(now + timedelta(hours=14))

# 本地时间转换为UTC时间
'''
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。一个datetime类型有一个时区
属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区。
'''
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
print(now)
dt2 = now.replace(tzinfo=tz_utc_8) # 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区
print(dt2)

# 时区转换
'''
可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间。

时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。

利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如下面的bj_dt到tokyo_dt的转换。
'''
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) # 拿到UTC时间，并强制设置时区为UTC+0:00
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8))) # astimezone()将转换时区为北京时间
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9))) # astimezone()将转换时区为东京时间
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9))) # astimezone()将bj_dt转换时区为东京时间
print(tokyo_dt2)
print(utc_dt.timestamp() == tokyo_dt.timestamp())
print(bj_dt.timestamp() == tokyo_dt.timestamp())

# 练习：假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
import re
def to_timestamp(dt_str, tz_str):
    m = re.match(r'^UTC([\+\-]\d{1,2}):00$', tz_str)
    tz_hours = int(m.group(1))
    # h = int(re.findall(r'^UTC([\+\-]\d{1,2}):00$', tz_str)[0])
    # print(h, re.findall(r'^UTC([\+\-]\d{1,2}):00$', tz_str))
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt = dt.replace(tzinfo=timezone(timedelta(hours=tz_hours)))
    return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('ok')

print('#'*10, '1.datetime', 'start' if 0 else 'end', '#'*10)



### 2.collections
'''
collections是Python内建的一个集合模块，提供了许多有用的集合类。
'''
print('#'*10, '2.collections', 'start' if 1 else 'end', '#'*10)
# namedtuple
'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
'''
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y']) # namedtuple('名称', [属性list])
print(Point)
pt = Point(1, 2)
print(pt, pt.x, pt.y, pt[0], pt[1])
print(isinstance(pt, Point), isinstance(pt, Point))

# deque
'''
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。deque除了实现list的append()和pop()外，还支持appendleft()
和popleft()，这样就可以非常高效地往头部添加或删除元素。
'''
from collections import deque
dq = deque(['a', 'b', 'c'])
print(dq)
dq.append('x')
dq.appendleft('y')
print(dq)
dq.insert(0, 'z')
print(dq)

# defaultdict
'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict。

注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。除了在Key不存在时返回默认值，defaultdict的其他
行为跟dict是完全一样的。
'''
from collections import defaultdict
dd = defaultdict(lambda :None)
dd['key1'] = 'abc'
print(dd, type(dd))
print(dd['key1'])
print(dd['key2'])

# OrderedDict
'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict。
'''
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict(d)
print(od, od2)
'''注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序'''
od3 = OrderedDict()
od3['z'] = 1; od3['x'] = 2; od3['y'] = 6
print(list(od3.keys()))
'''OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key'''
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__() # python3可使用super().__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

luod = LastUpdatedOrderedDict(2)
luod['z'] = 1; luod['x'] = 5
print(luod, type(luod))
luod['y'] = 9
print(luod)
luod['y'] = -6
print(luod)

# ChainMap
'''
ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在
内部的dict依次查找。

什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传
入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，
如果没有，就使用默认参数。

下面的代码演示了如何查找user和color这两个参数。
'''
from collections import ChainMap
import os, argparse

defaults = {'color': 'red', 'user': 'guest'} # 构造缺省参数

parser = argparse.ArgumentParser() # 构造命令行参数
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
cmd_line_args = {k: v for k, v in vars(namespace).items() if v}

combined = ChainMap(cmd_line_args, os.environ, defaults) # 组合成ChainMap

'''
没有任何参数时，打印出默认参数：
$ python3 use_chainmap.py 
color=red
user=guest

当传入命令行参数时，优先使用命令行参数：
$ python3 use_chainmap.py -u bob
color=red
user=bob

同时传入命令行参数和环境变量，命令行参数的优先级较高：
$ user=admin color=green python3 use_chainmap.py -u bob
color=green
user=bob
'''
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# Counter
'''
Counter是一个简单的计数器，Counter实际上也是dict的一个子类。
'''
from collections import Counter
ctr = Counter()
for ch in 'Programming': ctr[ch] += 1
print(ctr, ctr['P'])

print('#'*10, '2.collections', 'start' if 0 else 'end', '#'*10)



### 3.base64
'''
Base64是一种用64个字符来表示任意二进制数据的方法。

Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示
和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符
串的转换方法。Base64是一种最常见的二进制编码方法。

Base64的原理很简单，首先，准备一个包含64个字符的数组： ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit：
   b1      b2     b3
++++++++xxxxxxxx++++++++
------******------******
  n1    n2    n3    n4
这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。

所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本
数据可以在邮件正文、网页等直接显示。

XXX 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾
    补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
'''
print('#'*10, '3.base64', 'start' if 1 else 'end', '#'*10)
# Python内置的base64可以直接进行base64的编解码
import base64
b64enc = base64.b64encode(b'binary\x00string')
print(b64enc, type(b64enc), b64enc.decode('utf-8'))
b64dec = base64.b64decode(b64enc)
print(b64dec, type(b64dec), b64dec.decode('utf-8'))

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"
# 的base64编码，其实就是把字符+和/分别变成-和_
b64enc2 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b64enc2, type(b64enc2), b64enc2.decode('utf-8'))

b64enc3 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b64enc3, type(b64enc3), b64enc3.decode('utf-8'))

b64dec3 = base64.urlsafe_b64decode(b'abcd--__')
print(b64dec3, type(b64dec3))

'''
还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，不过，通常情况下完全没有必要。
Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉，
去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要
加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
'''
# 练习：请写一个能处理去掉=的base64解码函数
def safe_base64_decode(s):
    # if isinstance(s, str):
    #     enc_str = s
    # elif isinstance(s, bytes):
    #     enc_str = s.decode('utf-8')
    enc_str = str(s, encoding='utf-8')
    enc_str.replace('=', '')
    cnt = len(enc_str) % 4
    if cnt != 0: 
        enc_str += '='*(4-cnt)

    return base64.b64decode(enc_str)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

print('#'*10, '3.base64', 'start' if 0 else 'end', '#'*10)



### 4.struct
'''
Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。struct的pack函数把任意数据类型变成bytes。

详细使用可参考：https://docs.python.org/3/library/struct.html。
'''
print('#'*10, '4.struct', 'start' if 1 else 'end', '#'*10)
import struct
'''
pack的第一个参数是处理指令，'>I'的意思是：
>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。后面的参数个数要和处理指令一致。
'''
print(struct.pack('>I', 2048), struct.pack('>I', 10240099))
'''
下面的例子用unpack把bytes变成相应的数据类型：
根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。
'''
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
print(struct.unpack('<I', b'\x00\x08\x00\x00'))
# 取bmp前30个字节来分析
bmphead = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', bmphead))

# 练习：编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAA   \
                             EgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/   \
                             /3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8   \
                             AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9/   \
                             /38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8   \
                             AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8   \
                             AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8   \
                             AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9/   \
                             /3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8   \
                             AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8   \
                             AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8   \
                             AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/   \
                             /38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8   \
                             AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/   \
                             /3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
def bmp_info(data):
    bh = data[:30]
    unpack_bh = struct.unpack('<ccIIIIIIHH', bh)
    print(unpack_bh, bh)

    return {
        'width': unpack_bh[6],
        'height': unpack_bh[7],
        'color': unpack_bh[9]
    }

# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

print('#'*10, '4.struct', 'start' if 0 else 'end', '#'*10)



### 5.hashlib
'''
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，
不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证
用户口令。

摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

举个例子，你写了一篇文章，内容是一个字符串'how to use python hashlib - by Michael'，并附上这篇文章的摘要是
'2d73d4f15c0db7f5ecb321b6a65e5d6d'。如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，
你可以一下子指出Bob篡改了你的文章，因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。

可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
另一种常见的摘要算法是SHA1，SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
'''
print('#'*10, '5.hashlib', 'start' if 1 else 'end', '#'*10)
# 以常见的摘要算法MD5为例，计算出一个字符串的MD5值
import hashlib
# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5 = hashlib.md5('how to use md5 '.encode('utf-8'))
print(md5, md5.hexdigest())
md5.update('in python hashlib?'.encode('utf-8'))
print(md5, md5.hexdigest())

# 调用SHA1和调用MD5完全类似
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1, sha1.hexdigest())

'''
摘要算法能应用到什么地方？举个常用例子：
任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：
name	password
michael	123456
bob	    abc999
alice	alice2008
如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问
数据库的，也就是能获取到所有用户的口令。

正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
username	password
michael	    e10adc3949ba59abbe56e057f20f883e
bob      	878ef96e86145580c38c87f0410ad153
alice	    99b1c2188db85afee403b1536010c2c9
当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，
如果不一致，口令肯定错误。存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
'''
# 练习：根据用户输入的口令，计算出存储在数据库中的MD5口令
def calc_md5(password):
    md5 = hashlib.md5(password.encode('utf-8'))
    return md5.hexdigest()

# 练习：设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    ret = True if db[user] == calc_md5(password) else False
    return ret

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

'''
采用MD5存储口令是否就一定安全呢？也不一定。由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令
不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”。

经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。但是如果有两
个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。
有没有办法让使用相同口令的用户存储不同的MD5呢？如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部
分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
'''
def calc_md5_with_salt(password):
    return calc_md5(password + 'the-Salt')

# 练习：根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5，然后，根据修改后的MD5算法实现用户登录的验证
import random

db2 = {}

def register(username, password):
    db2[username] = calc_md5(password + username + 'the-Salt')

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = calc_md5(password + self.salt)

db3 = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login2(username, password):
    user = db3[username]
    return user.password == calc_md5(password + user.salt)

assert login2('michael', '123456')
assert login2('bob', 'abc999')
assert login2('alice', 'alice2008')
assert not login2('michael', '1234567')
assert not login2('bob', '123456')
assert not login2('alice', 'Alice2008')
print('ok')

print('#'*10, '5.hashlib', 'start' if 0 else 'end', '#'*10)



### 6.hmac
'''
哈希算法中，如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。但实际上，
把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不通口令计算出不同的哈希，
要验证哈希值，必须同时提供正确的口令。

这实际上就是Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算
哈希的过程中，把key混入计算过程中。和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通
用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，使用
hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。
'''
print('#'*10, '6.hmac', 'start' if 1 else 'end', '#'*10)
# 首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下
'''
使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key
和message都是bytes类型，str类型需要首先编码为bytes。
'''
import hmac
msg = b'Hello, world!'
key = b'secret'
hm = hmac.new(key, msg, digestmod='MD5')
print(hm.hexdigest())

# 练习：将上一节hashlib的salt改为标准的hmac算法，验证用户口令
def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User2(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db4 = {
    'michael': User2('michael', '123456'),
    'bob': User2('bob', 'abc999'),
    'alice': User2('alice', 'alice2008')
}

def login3(username, password):
    user = db4[username]
    return user.password == hmac_md5(user.key, password)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

print('#'*10, '6.hmac', 'start' if 0 else 'end', '#'*10)



### 7.itertools
'''
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
'''
print('#'*10, '7.itertools', 'start' if 1 else 'end', '#'*10)
import itertools

# count()会创建一个无限的迭代器，可以传入第2个参数以表示步长
naturals = itertools.count(6)
for n in naturals:
    if(n < 36):
        print(n)
    else:
        break

# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
cnt = 11
for c in cs:
    if cnt > 0:
        print(c)
        cnt -= 1
    else:
        break

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A0-', 3)
for n in ns:
    print(n)

'''
无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，
事实上也不可能在内存中创建无限多个元素。无限序列虽然可以无限迭代下去
'''
# 通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
naturals2 = itertools.count(1)
ns2 = itertools.takewhile(lambda x: x <= 10, naturals2)
print(list(ns2), ns2, type(ns2))

'''itertools提供的几个迭代器操作函数更加有用'''
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('abc', 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
'''
实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
而函数返回值作为组的key。
'''
# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
for key, group in itertools.groupby('AaaBBbcCAaAa', lambda c: c.upper()):
    print(key, list(group))
for key, group in itertools.groupby('AaaBBbcCAaAa'):
    print(key, list(group))

# 练习：计算圆周率
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    naturals = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    oddN = itertools.takewhile(lambda x: x <= 2*N-1, naturals)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    oddN2 = [4 / x * (-1)**i for i, x in enumerate(oddN)]
    # step 4: 求和:
    return sum(oddN2)

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

print('#'*10, '7.itertools', 'start' if 0 else 'end', '#'*10)



### 8.contextlib
'''
contextlib有一些decorator，便于我们编写更简洁的代码。
'''
print('#'*10, '8.contextlib', 'start' if 1 else 'end', '#'*10)
# 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法
# 是使用try...finally
try:
    f = open('E:/GITHUB/Python/course/0-连接.py', 'r', encoding='utf-8')
    ct = f.read()
    # print(ct)
finally:
    if f:
        f.close()
# 写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以
# 上面的代码可以简化为如下所示
with open('E:/GITHUB/Python/course/0-连接.py', 'r', encoding='utf-8') as f:
    f.read()

'''
并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的。
'''
# 下面的class实现了__enter__和__exit__这两个方法
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('begin')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('error')
        else:
            print('end')

    def query(self):
        print('Query info about %s...' % self.name)
# 这样我们就可以把自己写的资源对象用于with语句
with Query('Bob') as q:
    q.query()

# @contextmanager
# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下
from contextlib import contextmanager

class Query2(object):
    def __init__(self, name):
        self.name = name
    
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('begin')
    q = Query2(name)
    yield q
    print('end')

'''
@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就
可以正常地工作了。
'''
with create_query('David') as q:
    q.query()

'''
很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。

下面示例代码的执行顺序是：
with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。

因此，@contextmanager让我们通过编写generator来简化上下文管理。
'''
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

# closing
'''
如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。

closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
它的作用就是把任意对象变为上下文对象，并支持with语句。
'''
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)

print('#'*10, '8.contextlib', 'start' if 0 else 'end', '#'*10)



### 9.urllib
'''
urllib提供了一系列用于操作URL的功能。

urllib提供的功能就是利用程序去执行各种HTTP请求，如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器，
伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。
'''
print('#'*10, '9.urllib', 'start' if 1 else 'end', '#'*10)
# Get
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
from urllib import request

req = request.Request('https://www.baidu.com')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', data.decode('utf-8'))

# Post
# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入
# 我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入
from urllib import parse

print('Login to weibo.cn...')
# email = input('Email: ')
# pswd = input('Password: ')
email = ''
pswd = ''
login_data = parse.urlencode([
    ('username', email),
    ('password', pswd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', data.decode('utf-8'))

# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
proxy_handler = request.ProxyHandler({'http':'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass

# 练习：利用urllib读取JSON，然后将JSON解析为Python对象
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
    return json.loads(data.decode('utf-8'))

URL = 'https://www.easy-mock.com/mock/5cbec5d8bfb3b05625e96633/dreamlf/urllibTest'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')

print('#'*10, '9.urllib', 'start' if 0 else 'end', '#'*10)



### 10.XML
'''

'''
print('#'*10, '10.XML', 'start' if 1 else 'end', '#'*10)



print('#'*10, '10.XML', 'start' if 0 else 'end', '#'*10)



### 11.HTMLParser
'''

'''
print('#'*10, '11.HTMLParser', 'start' if 1 else 'end', '#'*10)



print('#'*10, '11.HTMLParser', 'start' if 0 else 'end', '#'*10)






