﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' course name：面向对象编程 '

__author__ = 'bingshuizhilian'



import sys



### 1.面向对象编程
# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
# 面向对象的设计思想是抽象出Class，根据Class创建Instance；数据封装、继承和多态是面向对象的三大特点。
print('#'*10, '1.面向对象编程', 'start' if 1 else 'end', '#'*10)
class Student(object):
    __slots__ = ('name', 'score', 'age')

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90: return 'A'
        elif self.score >= 80: return 'B'
        elif self.score >= 60: return 'C'
        else: return 'D'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
lilyDict = {'name': 'lily', 'score': 99}
lily = Student(**lilyDict)
bart.print_score()
lisa.print_score()
lily.print_score()

print('#'*10, '1.面向对象编程', 'start' if 0 else 'end', '#'*10)



### 2.类和实例
'''
1.定义类是通过class关键字，class后面紧接着是类名，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，
  通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
2.类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。类通过定义一个特殊的__init__方法，
  可以预先为每个实例都绑定一些属性(实质类似于C++数据成员)。
3.注意到__init__方法的第一个参数永远是self，表示创建的实例本身(实质类似于C++的this指针)，因此，在__init__方法内部，就可以把各
  种属性绑定到self，因为self就指向创建的实例本身。
4.有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己
  会把实例变量传进去。
5.和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的
  方法和普通函数没有什么区别，所以，仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
6.和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称
  都可能不同，如下面bart.age
'''
print('#'*10, '2.类和实例', 'start' if 1 else 'end', '#'*10)
bart.age = 19  # 可以自由地给一个“实例”(注意是绑定在实例上，而非类里)变量绑定属性，比如，给实例bart绑定一个age属性
print(bart.age)
print('#'*10, '2.类和实例', 'start' if 0 else 'end', '#'*10)



### 3.数据封装
'''
1.实例本身拥有数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在类的内部定义访问数据的函数，这样，
  就把“数据”给封装起来了。这些封装数据的函数是和类本身是关联起来的，称之为类的方法(methord)。
2.要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了
  self不用传递，其他参数正常传入。
'''
print('#'*10, '3.数据封装', 'start' if 1 else 'end', '#'*10)
print(bart.name, bart.get_grade())
print('#'*10, '3.数据封装', 'start' if 0 else 'end', '#'*10)



### 4.访问限制
'''
1.实例本身拥有数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在类的内部定义访问数据的函数，这样，
  就把“数据”给封装起来了。这些封装数据的函数是和类本身是关联起来的，称之为类的方法(methord)。
2.要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了
  self不用传递，其他参数正常传入。
3.如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变
  成了一个私有变量（private），只有内部可以访问，外部不能访问，这样就确保了外部代码不能随意修改对象内部的状态。
4.需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊
  变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
5.有些时候，会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成
  的规定，当看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
6.不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name
  来访问__name变量，但是强烈建议不要这么写，因为不同版本的Python解释器可能会把__name改成不同的变量名。
7.最后注意下面的这种错误写法：bart.__name = 'New Name' 。表面上看，外部代码“成功”地设置了__name变量，但实际上
  这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，
  而外部代码给bart新增了一个__name变量。
'''
print('#'*10, '4.访问限制', 'start' if 1 else 'end', '#'*10)
class Student2(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90: return 'A'
        elif self.__score >= 80: return 'B'
        elif self.__score >= 60: return 'C'
        else: return 'D'
    
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

lucy = Student2('lucy', 89)
# print(lucy.__name)  # 现在还不能调用
lucy.__name = 'new name'
print('real: ', lucy._Student2__name, ', fake: ', lucy.__name)
print(lucy.get_name())
lucy.set_name('lucy lucy')
print(lucy.get_name())

print('#'*10, '4.访问限制', 'start' if 0 else 'end', '#'*10)



### 5.继承和多态
# 继承最大的好处是子类获得了父类的全部功能。
# 当子类和父类都存在相同的方法时，子类覆盖了父类的方法，在代码运行的时候，总是会调用子类的方法。这就是继承的另一个好处：多态。
# “开闭”原则，对扩展开放：允许新增子类；对修改封闭：不需要修改依赖该类型的函数。 
# 把不同的子类对象都当作父类来看，可以屏蔽不同子类对象之间的差异，写出通用的代码，做出通用的编程，以适应需求的不断变化。
print('#'*10, '5.继承和多态', 'start' if 1 else 'end', '#'*10)
class Animal:
    unionParam = 50
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    unionParam = 90
    def run2(self):
        print('Animal is running...')

class Fox(Animal):
    unionParam = -26
    def __init__(self, param):
        self.unionParam = param
    
    def run(self):
        print('Wolf is running...')

class FoxSon(Fox):pass

def run_test(animal):
    animal.run()

base = Animal()
dog = Dog()
cat = Cat()

run_test(base)
run_test(dog)
run_test(cat)

print(isinstance(cat, Animal), isinstance(cat, Cat))
print(cat.unionParam)
cat.unionParam = 10
dog.unionParam = 20
print(base.unionParam, cat.unionParam, dog.unionParam)

fox = Fox(31)
print(fox.unionParam)
foxson = FoxSon(45)
print(foxson.unionParam)

# 静态语言 vs 动态语言
'''
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了，这就是动态语言
的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。动态语言的鸭子
类型特点决定了继承不像静态语言那样是必须的。
'''

# 题外话：观察是否写了继承自object的区别，实际在python3中，类均默认继承自object。
class aa:pass
class bb():pass
class cc(object):pass
print('*'*20, dir(Student2), '*'*20)
print('*'*20, dir(aa), '*'*20)
print('*'*20, dir(bb), '*'*20)
print('*'*20, dir(cc), '*'*20)
print('#'*10, '5.继承和多态', 'start' if 0 else 'end', '#'*10)



### 6.获取对象信息
print('#'*10, '6.获取对象信息', 'start' if 1 else 'end', '#'*10)
# 使用type()
# 基本类型都可以用type()判断。
print(type(foxson), type('123'), 123 == type(int), type(run_test), type(max))
print(type(lambda x:x), type((x for x in range(9))))

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数，
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
print(isinstance(dog, Dog), isinstance(dog, Animal), isinstance(base, Dog))
# isinstance()还可以判断一个变量是否是某些类型中的一种
print(isinstance([1,2], (list, tuple)))
print(isinstance((1,2), (list, tuple)))

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list。
print(dir('abc'), dir(str) == dir('abc'))

# 使用getattr()、setattr()以及hasattr()操作一个对象的状态
# 要注意的是，只有在不知道对象信息的时候，才会去获取对象信息。
print(hasattr(base, 'run'), hasattr(dog, 'favourite'))
print(getattr(base, 'run'))
setattr(dog, 'favourite', 'bone')
if hasattr(dog, 'favourite'):
    print(getattr(dog, 'favourite'))

print('#'*10, '6.获取对象信息', 'start' if 0 else 'end', '#'*10)



### 7.实例属性和类属性
'''
由于Python是动态语言，根据类创建的实例可以任意绑定属性，给实例绑定属性的方法是通过实例变量，或者通过self变量。
如果类本身需要绑定一个属性，可以直接在class中定义属性，这种属性是类属性，归类所有，这个属性虽然归类所有，但类
的所有实例都可以访问到。
'''
print('#'*10, '7.实例属性和类属性', 'start' if 1 else 'end', '#'*10)

print(base.unionParam, Animal.unionParam)
base.unionParam = 'override unionParam'
print(base.unionParam, Animal.unionParam)
# 可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽
# 掉类属性，但是当删除实例属性后，再使用相同的名称，访问到的将是类属性。

print('#'*10, '7.实例属性和类属性', 'start' if 0 else 'end', '#'*10)
