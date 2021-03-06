﻿#!/usr/bin/env python3
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
# Python的class中有许多像__slots__这样有特殊用途的函数，可以实现定制类。
print('#'*10, '5.定制类', 'start' if 1 else 'end', '#'*10)
class CustomizedDemo(object):
    def __init__(self, name):
        self.__name = name

    # __str__()返回用户看到的字符串
    def __str__(self):
        return 'CustomizedDemo object (name: %s)' % self.__name

    # __repr__()返回程序开发者看到的字符串，为调试服务
    __repr__ = __str__

cdobj = CustomizedDemo("cdobj")
print(cdobj, CustomizedDemo("cdobj2"))

'''
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:  # 退出循环的条件
            raise StopIteration()
        return self.a

    # 要像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, n):
        print('Fib __getitem__ param n =', n)
        a, b = 1, 1

        if isinstance(n, int):
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            # step = n.step  # step是步进值，此外，切片slice的负值亦未处理
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for x in Fib():
    print(x)

print(Fib()[5], Fib()[100], Fib()[3:5], Fib()[:5])

''' ↑ 关于__setitem__和__delitem__：
如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个
__delitem__()方法，用于删除某个元素。
'''

class CustomizedDemo2(object):
    def __init__(self, name):
        self.__name = name

    # 调用类的方法或属性时，如果不存在会报错。要避免这个错误，除了可以加上一个属性外，
    # Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
    def __getattr__(self, attr):
        if 'age' == attr:
            return 20  # 返回属性

        if 'score' == attr:
            return lambda :25  # 返回方法

        raise AttributeError('CustomizedDemo2 object has no attribute \'%s\'' % attr)

    # 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
    def __call__(self):
        print('CustomizedDemo2 object name is \'%s\'' % self.__name)

'''
注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性不会在__getattr__中查找。
__getattr__默认返回None，要让class只响应特定的几个属性，就要按照约定，抛出AttributeError异常。
'''
cd2obj = CustomizedDemo2('cd2obj')
print(cd2obj.age, cd2obj.score, cd2obj.score())
# print(cd2obj.year)  # 当__getattribute__有raise AttributeError时会抛出异常；否则__getattr__默认返回None
print(callable(cd2obj))
cd2obj()
print(dir(cd2obj))

print('#'*10, '5.定制类', 'start' if 0 else 'end', '#'*10)



### 6.使用枚举类
# 当我们需要定义常量时，好的方法是为这样的枚举类型定义一个class类型，然后，
# 每个常量都是class的一个唯一实例，Python提供了Enum类来实现这个功能。
print('#'*10, '6.使用枚举类', 'start' if 1 else 'end', '#'*10)
from enum import Enum, unique

# value属性则是自动赋给成员的int常量，默认从1开始计数。
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Month.Jan, Month['Feb'], Month.Mar.value)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)

day = Weekday.Mon
print(type(day), day, day.value)
print(Weekday.Tue, Weekday['Sun'], Weekday.Thu.value)
print(day == Weekday.Mon, day == Weekday(1), Weekday(5))
# Weekday(7)  # 不能运行，无此值

# ↑ 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。

print('#'*10, '6.使用枚举类', 'start' if 0 else 'end', '#'*10)



### 7.使用元类
print('#'*10, '7.使用元类', 'start' if 1 else 'end', '#'*10)
'''
1.class的定义是运行时动态创建的，而创建class的方法就是使用type()函数；通过type()函数
  创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class
  定义的语法，然后调用type()函数创建出class；动态语言本身支持运行期动态创建类。
2.type()函数既可以返回一个对象的类型，又可以创建出新的类型。
3.要创建一个class对象，type()函数依次传入3个参数：
(1)class的名称；
(2)继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
(3)class的方法名称与函数绑定。
'''
def TypeBindindFunctionDemo(self, name = 'world'):
    print('Hello, %s' % name)

Hello = type('Hello', (object, ), dict(hello = TypeBindindFunctionDemo))
h = Hello()
h.hello()
print(type(Hello), type(h))

'''
1.除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
  metaclass，直译为元类，简单的解释就是：先定义metaclass，就可以创建类，最后创建实例。
  metaclass允许创建类或者修改类，可以把类看成是metaclass创建出来的“实例”。
'''
# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

'''
1.有了ListMetaclass，在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass。
2.当传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()
  来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
3.__new__()方法接收到的参数依次是：当前准备创建的类的对象；类的名字；类继承的父类集合；类的方法集合。
'''
class MyList(list, metaclass = ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)
L2 = []
# L2.add(2)  # 不能运行
print(L2)

'''
《通过metaclass修改类定义的例子：ORM》
ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
这样，写代码更简单，不用直接操作SQL语句。要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定
义出对应的类来。
'''
# 定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(255)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# 接下来是最复杂的ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if 'Model' == name:
            return type.__new__(cls, name, bases, attrs)

        print('Found model: %s' % name)

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s => %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致

        return type.__new__(cls, name, bases, attrs)

# 基类Model
class Model(dict, metaclass = ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    def query(self):
        pass

# 编写底层模块的第一步，先写调用接口，但由于编译的关系，需要把这步放到下面
'''
其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如query()全部由metaclass自动
完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。
'''
class movie_top250(Model):
    # 定义类的属性到列的映射
    title = StringField('title')
    movieInfo = StringField('movieInfo')
    star = StringField('star')
    evaluation = StringField('evaluation')
    quote = StringField('quote')
    unusedItem = IntegerField('unusedItem')

m = movie_top250(star = '9.4')
m.query()
m.save()

'''
1.当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，如果没有找到，
  就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，
  也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。
2.在ModelMetaclass中，一共做了几件事情：
(1)排除掉对Model类的修改；
(2)在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__
   的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
(3)把表名保存到__table__中，这里简化为表名默认为类名。
3.在Model类中，可以定义各种操作数据库的方法，比如save()，delete()，find()，update等。
4.我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。
'''
print('#'*10, '7.使用元类', 'start' if 0 else 'end', '#'*10)
