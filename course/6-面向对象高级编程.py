#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' course name：面向对象高级编程 '

__author__ = 'bingshuizhilian'



### 1.面向对象高级编程
# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念，在Python中，面向对象还有很多高级特性，
# 如多重继承、定制类、元类等概念。
print('#'*10, '1.面向对象高级编程', 'start' if 1 else 'end', '#'*10)
# 创建了一个class的实例后，可以给该实例绑定任何属性和方法，这是动态语言的灵活性，还可以给实例绑定一个方法，如：
from types import MethodType

class Student: pass
def set_age(self, age): self.age = age

s = Student()
s2 = Student()
print(dir(s))
s.set_age = MethodType(set_age, s) # 给一个实例绑定的方法，对另一个实例不起作用
s.set_age(25)
# s2.set_age(20) # 不能运行
print(s.age)
print(dir(s))

Student.set_age = set_age # 将方法绑定到类中
s2.set_age(20) # 现在可以运行了
print(s2.age)
print('#'*10, '1.面向对象高级编程', 'start' if 0 else 'end', '#'*10)



### 2.使用__slots__
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性。
print('#'*10, '2.使用__slots__', 'start' if 1 else 'end', '#'*10)
class Student2:
    __slots__ = ('__name')

    def __init__(self, name):
        self.__name = name

    def print_name(self):
        print(self.__name)

print(Student2.__slots__)
s3 = Student2('lily')
s3.print_name()

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的，除非在子类中也定义__slots__。
class GraduatedStudent(Student2):
    pass

gs = GraduatedStudent('lilei')
gs.print_name()
gs.age = 18
print(gs.age)

class GraduatedStudent2(Student2): 
    __slots__ = ('__age')

print(GraduatedStudent2.__slots__)
gs2 = GraduatedStudent2('lucy')
gs2.print_name()
# gs2.age = 18 # 不能运行
print('#'*10, '2.使用__slots__', 'start' if 0 else 'end', '#'*10)



### 3.使用@property
# @property 可以将 getter方法转换成属性调用，而@property创建的对应的装饰器@xxx.setter可以把setter方法转换成属性赋值。
print('#'*10, '3.使用@property', 'start' if 1 else 'end', '#'*10)
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, h):
        self._height = h

    @property
    def resolution(self):
        return self._width * self._height


scn = Screen()
scn.width = 1024
print(scn.width)
scn.height = 768
print(scn.height)
print(scn.resolution)
# scn.resolution = 89 # 不能运行，未设置setter方法，相当于只读属性

print('#'*10, '3.使用@property', 'start' if 0 else 'end', '#'*10)



### 4.多重继承
'''
(1).在设计类的继承关系时，通常，主线都是单一继承下来的，但是，如果需要“混入”额外的功能，
通过多重继承就可以实现，这种设计通常称之为MixIn。
(2).MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承
来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。这样一来，我们不需要复杂而庞大的
继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。
'''
print('#'*10, '4.多重继承', 'start' if 1 else 'end', '#'*10)
class TCPServer:
    pass

class ForkingMixIn:
    pass

class MyTCPServer(TCPServer, ForkingMixIn):
    pass

# 以下2例参考自此网页: https://www.jianshu.com/p/c9a0b055947b
# MRO例1
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A,B):
    pass

class C2(A,B):
    def bar(self):
        print('C2-bar')

class D(C1,C2):
    pass

print(D.__mro__)
d=D()
d.foo()
d.bar()

# MRO例2
class A2(object):
    def foo(self):
        print('A2 foo')
    def bar(self):
        print('A2 bar')

class B2(object):
    def foo(self):
        print('B2 foo')
    def bar(self):
        print('B2 bar')

class C3(A2):
    pass

class C4(B2):
    def bar(self):
        print('C4-bar')

class D2(C3,C4):
    pass

print(D2.__mro__)
d2=D2()
d2.foo()
d2.bar()

print('#'*10, '4.多重继承', 'start' if 0 else 'end', '#'*10)



### 5.定制类
print('#'*10, '5.定制类', 'start' if 1 else 'end', '#'*10)




print('#'*10, '5.定制类', 'start' if 0 else 'end', '#'*10)
