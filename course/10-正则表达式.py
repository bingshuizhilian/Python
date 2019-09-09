#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' course name：正则表达式 '

__author__ = 'bingshuizhilian@yeah.net'



import re

### 1.正则表达式
r'''
正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串
定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

一些规则
基础部分：
在正则表达式中，如果直接给出字符，就是精确匹配，
\d可以匹配一个数字，
\w可以匹配一个字母或数字，
\s可以匹配一个空格（也包括Tab等空白符），
.可以匹配任意字符，要匹配变长的字符，
*表示任意个字符（包括0个），
+表示至少一个字符，
?表示0个或1个字符，
{n}表示n个字符，
{n,m}表示n-m个字符，
特殊字符，要用'\'转义。

进阶部分：
精确匹配，可以用[]表示范围（如[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串），
A|B可以匹配A或B，
^表示行的开头，^\d表示必须以数字开头，
$表示行的结束，\d$表示必须以数字结束。
'''
print('#'*10, '1.正则表达式', 'start' if 1 else 'end', '#'*10)

print('#'*10, '1.正则表达式', 'start' if 0 else 'end', '#'*10)



### 2.re模块
r'''
Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，
因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了。
'''
print('#'*10, '2.re模块', 'start' if 1 else 'end', '#'*10)
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
print(re.match(r'^\d{3}\-\d{3,8}', '010-123456789'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345678'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010-123456789'))
print('#'*10, '2.re模块', 'start' if 0 else 'end', '#'*10)



### 3.切分字符串
# 用正则表达式切分字符串比用固定的字符更灵活
print('#'*10, '3.切分字符串', 'start' if 1 else 'end', '#'*10)
# 正常的切分代码
print('a b   c'.split(' '))
# 正则表达式切分代码
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s,]+', 'a,b, c  d'))
print(re.split(r'[\s,;]+', 'a,b, c  d;;  ; e'))
print('#'*10, '3.切分字符串', 'start' if 0 else 'end', '#'*10)



### 4.分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能，用()表示的就是要提取的分组（Group）
print('#'*10, '4.分组', 'start' if 1 else 'end', '#'*10)
# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来，注意到group(0)永远是原始
# 字符串，group(1)、group(2)、……表示第1、2、……个子串
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m, m.groups(), m.group(0), m.group(1), m.group(2))
print('#'*10, '4.分组', 'start' if 0 else 'end', '#'*10)



### 5.贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符，加个?就可以让\d+采用非贪婪匹配
print('#'*10, '5.贪婪匹配', 'start' if 1 else 'end', '#'*10)
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
m2 = re.match(r'^(\d+)(0*)$', '102300')
print(m2.groups())
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
m3 = re.match(r'^(\d+?)(0*)$', '102300')
print(m3.groups())
m4 = re.match(r'^(\d+?)(0*?)$', '1023000')
print(m4.groups())
print('#'*10, '5.贪婪匹配', 'start' if 0 else 'end', '#'*10)



### 6.编译
'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：1、编译正则表达式，如果正则表达式的字符串本身不合法，
会报错；2、用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这
个步骤了，可以直接匹配。

编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
'''
print('#'*10, '6.编译', 'start' if 1 else 'end', '#'*10)
# 第一步：编译
m5 = re.compile(r'^(\d{3})-(\d{3,8})$')
m6 = re.compile(r'^\d{3}-\d{3,8}$')
# 第二步，使用
print(m5.match('010-12345').groups())
print(m6.match('010-8086'))
print('#'*10, '6.编译', 'start' if 0 else 'end', '#'*10)



### 7.练习
print('#'*10, '7.练习', 'start' if 1 else 'end', '#'*10)
# 练习1：请尝试写一个验证Email地址的正则表达式
def is_valid_email(addr):
    m = re.match(r'^\w[\w\.]*@\w+\.\w+$', addr)
    return True if m else False
    
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


# 练习2：可以提取出带名字的Email地址
def name_of_email(addr):
    m = re.match(r'^<([\w ]+)>[\w\. ]*@\w+\.\w+$', addr)
    if None == m:
        m = re.match(r'^(\w+)@\w+\.\w+$', addr)
    return m.group(1) if None != m else None

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
print('#'*10, '7.练习', 'start' if 0 else 'end', '#'*10)
