#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' course name：常用第三方模块 '

__author__ = 'bingshuizhilian'



'''
除了内建的模块外，Python还有大量的第三方模块。
基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用pip安装。
'''
### 1.Pillow
'''
Python Imaging Library，Pillow是python下的图像处理库，提供方便的接口来操作图像

提供缩放、切片、旋转、滤镜、输出文字、调色板等功能
'''
print('#'*10, '1.Pillow', 'start' if 1 else 'end', '#'*10)
from PIL import Image

## 图像缩放
im = Image.open('12-Pillow-china.jpg')
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# im.save('12-Pillow-china-resized.jpg', 'jpeg')
# im.show()

## 图像模糊
from PIL import ImageFilter

# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
# im2.show()

## PIL的ImageDraw提供了一系列绘图方法，可以直接绘图
# 生成字母验证码图片
from PIL import ImageDraw, ImageFont
import random

def rndChar():
    return chr(random.randint(65, 90))

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

w2 = 60 * 4
h2 = 60

im3 = Image.new('RGB', (w2, h2), (255, 255, 255))
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
draw = ImageDraw.Draw(im3)

for x in range(w2):
    for y in range(h2):
        draw.point((x, y), fill=rndColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

im3 = im3.filter(ImageFilter.BLUR)
# im3.show()

print('#'*10, '1.Pillow', 'start' if 0 else 'end', '#'*10)



### 2.requests
'''
requests是一个Python第三方库，处理URL资源特别方便
'''
print('#'*10, '2.requests', 'start' if 1 else 'end', '#'*10)
import requests

# 通过GET访问一个页面
# 需要传入HTTP Header时，传入一个dict作为headers参数
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
r = requests.get('https://www.douban.com', headers=headers)  
print(r.status_code)
# print(r.content)

# 对于带参数的URL，传入一个dict作为params参数
r2 = requests.get('https://www.douban.com/search', params={'q':'python', 'cat':'1001'}, headers=headers)
print(r2.url)

# requests自动检测编码，可以使用encoding属性查看
print(r2.encoding)

# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象
# print(r2.content)

# requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取
# r3 = requests.get(r'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json', headers=headers)
# print(r3.json())

# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据
r4 = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数
params = {'key': 'value'}
r5 = requests.post("https://www.baidu.com", json=params) # 内部自动序列化为JSON
# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数
# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度
# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源
upload_files = {'file': open('12-Pillow-china.jpg', 'rb')}
r6 = requests.post("https://www.baidu.com", files=upload_files)

# 除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头
print(r.headers)
print(r.headers['Content-Type'])

# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie
print(r.cookies)
# print(r.cookies['ts'])
# 要在请求中传入Cookie，只需准备一个dict传入cookies参数
cs = {'token': '12345', 'status': 'working'}
r7 = requests.get("https://www.baidu.com", cookies=cs)
print(r7.status_code)

# 要指定超时，传入以秒为单位的timeout参数
r8 = requests.get("https://www.baidu.com", timeout=2.5)
print(r8.status_code)

print('#'*10, '2.requests', 'start' if 0 else 'end', '#'*10)



### 3.chardet
'''
字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。虽然Python提供了Unicode表示的str和bytes两种数据类
型，并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes做decode()不好做。

对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。

当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。

用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理。

chardet支持检测的编码列表请参考官方文档https://chardet.readthedocs.io/en/latest/supported-encodings.html。
'''
print('#'*10, '3.chardet', 'start' if 1 else 'end', '#'*10)
import chardet

# 用chardet检测编码，只需要一行代码
print(chardet.detect(b'Hello, world!'))
dataGbk = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(dataGbk))
dataUtf8 = '离离原上草，一岁一枯荣'.encode('utf8')
print(chardet.detect(dataUtf8))
dataJp = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(dataJp))

print('#'*10, '3.chardet', 'start' if 0 else 'end', '#'*10)



### 4.psutil
'''
用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。
要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。

在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码
实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

psutil使得Python程序获取系统信息变得易如反掌。
psutil还可以获取用户信息、Windows服务等很多有用的系统信息，具体请参考psutil的官网：https://github.com/giampaolo/psutil
'''
print('#'*10, '4.psutil', 'start' if 1 else 'end', '#'*10)
import psutil

# 获取CPU的信息
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

# 统计CPU的用户／系统／空闲时间
print(psutil.cpu_times())

# CPU使用率，每秒刷新一次，累计10次
for _ in range(2):
    print(psutil.cpu_percent(interval=1, percpu=True))

# 获取物理内存和交换内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 获取磁盘分区、磁盘使用率和磁盘IO信息
print(psutil.disk_partitions())
print(psutil.disk_usage('c:/'))
print(psutil.disk_io_counters())

# 获取网络接口和网络连接信息
print(psutil.net_io_counters())
print(psutil.net_if_addrs())
print(psutil.net_if_stats())
print(psutil.net_connections())

# 获取到所有进程的详细信息
print(psutil.pids()) # 所有进程ID
p = psutil.Process()
print(p.name()) # 进程名称
print(p.exe()) # 进程exe路径
print(p.cwd()) # 进程工作目录
print(p.cmdline()) # 进程启动的命令行
print(p.ppid()) # 父进程ID
print(p.parent()) # 父进程
print(p.children()) # 子进程列表
print(p.status()) # 进程状态
print(p.username()) # 进程用户名
print(p.create_time()) # 进程创建时间
# print(p.terminal()) # 进程终端
print(p.cpu_times()) # 进程使用的CPU时间
print(p.memory_info()) # 进程使用的内存
print(p.open_files()) # 进程打开的文件
print(p.connections()) # 进程相关网络连接
print(p.num_threads()) # 进程的线程数量
print(p.threads()) # 所有线程信息
print(p.environ()) # 进程环境变量
# print(p.terminate()) # 结束进程

# psutil还提供了一个test()函数，可以模拟出ps命令的效果
print(psutil.test())


print('#'*10, '4.psutil', 'start' if 0 else 'end', '#'*10)

