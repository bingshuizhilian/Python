#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' course name：错误、调试和测试 '

__author__ = 'bingshuizhilian'



### 1.错误处理
print('#'*10, '1.错误处理', 'start' if 1 else 'end', '#'*10)
'''
1.当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续
  代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，
  如果有finally语句块，则执行finally语句块，至此，执行完毕。
2.finally如果有，则一定会被执行(可以没有finally语句)。
3.可以有多个except来捕获不同类型的错误。
4.如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句。
5.Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要
  注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
'''
try:
    print('try...')
    # r = 10 / 0
    # r = 10 / int('a')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except ZeroDivisionError:', e)
except ValueError as e:
    print('except ValueError:', e)
else:
    print('no error')
finally:
    print('finally...')
print('END')

'''
使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，
foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理；也就是说，不需要在
每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写
try...except...finally的麻烦。
'''
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except ZeroDivisionError as e:
        print('error', e)
    finally:
        print('finally...')

print('main')
main()

'''
调用栈
1.如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
2.Traceback (most recent call last): 告诉我们这是错误的跟踪信息。
3.出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
'''
def main2():
    bar('0')

print('main2')
# main2()

'''
记录错误
1.如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，
  就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
2.Python内置的logging模块可以非常容易地记录错误信息；通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
'''
import logging, os

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
 
# logging.basicConfig(filename=os.path.dirname(__file__) + '/my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

def main3():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

print('main3')
# main3()

'''
抛出错误
错误是class，捕获一个错误就是捕获到该class的一个实例。错误并不是凭空产生的，而是有意创建并抛出的。Python的
内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
'''

# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
class FooError(ValueError):
    def __init__(self, msg, value):
        self.__msg = msg
        self.__value = value

    def __str__(self):
        return '{}: {}'.format(self.__msg, self.__value)

def foo2(s):
    n = int(s)
    if 0 == n:
        raise FooError('invalid value', n)
    return 10 / n

# foo2('0')

try:
    raise FooError('FooError invalid value', 5)
except FooError as e:
    print(e)

# raise语句如果不带参数，就会把当前错误原样抛出
def bar2():
    try:
        foo2('0')
    except ValueError as e:
        logging.exception(e)
        print('ValueError!')
        raise

# bar2()

# 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型；
# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError
try:
    10 / 0
except ZeroDivisionError:
    # raise ValueError('input error!')
    print('input error!')

'''
1.只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
  尽量使用Python内置的错误类型。
2.Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。
3.程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。
'''

print('#'*10, '1.错误处理', 'start' if 0 else 'end', '#'*10)



### 2.调试
print('#'*10, '2.调试', 'start' if 1 else 'end', '#'*10)
# 方法一：print()
# 用print()把可能有问题的变量打印出来，简单直接粗暴有效，用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，
# 运行结果也会包含很多垃圾信息。

# 方法二：assert，即断言
# 凡是用print()来辅助查看的地方，都可以用断言(assert)来替代。
def foo3(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

# foo3('0')
'''
assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错，
如果断言失败，assert语句本身就会抛出AssertionError。

程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数
来关闭assert：$ python -O xxx.py。断言的开关“-O”是英文大写字母O，不是数字0。关闭后，可以把
所有的assert语句当成pass来看。
'''

# 方法三：logging
# 和assert比，logging不会抛出错误，而且可以输出到文件
# logging.basicConfig(filename=os.path.dirname(__file__) + '/my2.log', level=logging.ERROR, format=LOG_FORMAT, datefmt=DATE_FORMAT)
s_logging = '0'
n_logging = int(s_logging)
logging.info('n_logging = %d' % n_logging)
logging.error('n_logging = %d ..' % n_logging)
logging.exception('n_logging = %d ...' % n_logging)
# print(10 / n_logging)

'''
这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info
就不起作用了。这样一来，可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
'''

# 方法四：pdb
'''
启动Python的调试器pdb: $ python -m pdb xxx.py，让程序以单步方式运行，可以随时查看运行状态。

以参数-m pdb启动后，pdb定位到下一步要执行的代码，输入命令l来查看代码、输入命令n可以单步执行代码、
任何时候都可以输入命令p 变量名来查看变量、输入命令q结束调试，退出程序。这种通过pdb在命令行调试的
方法理论上是万能的，但是太麻烦。
'''

# 方法五：pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个
# pdb.set_trace()，就可以设置一个断点，运行代码，程序会自动在pdb.set_trace()暂停并进入pdb
# 调试环境，可以用命令p查看变量，或者用命令c继续运行，这个方式比直接启动pdb单步调试效率要高
# 很多，但也高不到哪去。
import pdb

s_logging2 = '0'
n_logging2 = int(s_logging2)
logging.info('n_logging2 = %d' % n_logging2)
logging.error('n_logging2 = %d ..' % n_logging2)
logging.exception('n_logging2 = %d ...' % n_logging2)
# pdb.set_trace()
# print(10 / n_logging2)

# 方法六：IDE
'''
如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：
[Visual Studio Code + Python插件]、PyCharm、[Eclipse + pydev插件]。

虽然用IDE调试起来比较方便，但是最后会发现，logging才是终极武器。
'''
print('#'*10, '2.调试', 'start' if 0 else 'end', '#'*10)



### 3.单元测试
'''
单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
'''
print('#'*10, '3.单元测试', 'start' if 1 else 'end', '#'*10)

import unittest

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        
        return 'C'

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()

print('#'*10, '3.单元测试', 'start' if 0 else 'end', '#'*10)

