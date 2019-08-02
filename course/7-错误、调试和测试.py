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



print('#'*10, '2.调试', 'start' if 0 else 'end', '#'*10)

