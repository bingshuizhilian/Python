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
