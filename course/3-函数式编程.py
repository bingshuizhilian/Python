# -*- coding: utf-8 -*-

from functools import reduce


# 1.传入函数/高阶函数
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式
print('#'*10, '1.传入函数/高阶函数', 'start' if 1 else 'end', '#'*10)
def add(a, b, f):
        return f(a) + f(b)

print(add(-6, 9, abs))
print('#'*10, '1.传入函数/高阶函数', 'start' if 0 else 'end', '#'*10)

# 2.map
# map()将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
print('#'*10, '2.map', 'start' if 1 else 'end', '#'*10)
def f(x):
        return x**2

r1 = map(f, [x for x in range(9)])
print(r1, type(r1), list(r1))
L1 = list(map(str, [x for x in range(9)]))
print(L1)

origList = [1,2,3];factor = 10
print([i * factor for i in origList])
print(list(map(lambda i:i*factor, origList)))

def normalize(name):
    return name[0].upper() + name[1:].lower() # name[0] == name[:1]

L2 = ['adam', 'LISA', 'barT']
L3 = list(map(normalize, L2))
print(L3)
print('#'*10, '2.map', 'start' if 0 else 'end', '#'*10)

# 3.reduce
# reduce()把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。
print('#'*10, '3.reduce', 'start' if 1 else 'end', '#'*10)
r2 = reduce(lambda x,y:x+y, [x for x in range(9)])
print(r2)
r3 = reduce(lambda x,y:x*10+y, [x for x in range(9) if x%2 == 1])
print(r3)
r4 = reduce(lambda x,y:x*10+y, map(int, [str(x) for x in range(10) if x%2 == 1]))
print(r4)

def str2int(s):
    yield reduce(lambda x,y:x*10+y, [int(z) for z in s])
    yield reduce(lambda x,y:x*10+y, map(int, [z for z in s]))

g1 = str2int('156984')
# for i in g1:
#     print(i)
print(next(g1))
print(next(g1))
try:
    print(next(g1))
except StopIteration as s:
    print('iter stoped......')
else:
    print('no exception......')
finally:
    print('over......')

def prod(L):
    return reduce(lambda x,y:x*y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(s):
    l=s.split(".")
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    # methord 1
    return reduce(lambda x,y:x*10+y, map(lambda i:d[i], l[0]+l[1])) / (10**len(l[1]))
    # methord 2
    # return reduce(lambda x,y:x*10+y, list(map(lambda i:d[i], l[0]))) + reduce(lambda x,y:(x*0.1+y), list(map(lambda i:d[i], l[1][::-1])))*0.1
print('str2float(\'123.456789\') =', str2float('123.456789'))
print('#'*10, '3.reduce', 'start' if 0 else 'end', '#'*10)

# 4.filter
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
print('#'*10, '4.filter', 'start' if 1 else 'end', '#'*10)
# and: 只要左边的表达式为真，整个表达式返回的值是右边表达式的值，否则，返回左边表达式的值
# or : 只要两边的表达式为真，整个表达式的结果是左边表达式的值；如果是一真一假，返回真值表达式的值；如果两个都是假，比如空值和0，返回的是右边的值。（空值或0）
L4 = list(filter(lambda s:s and s.strip(), ['A', '', 'B', None, 'C', '  ']))
print(L4)

# 素数
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_dividable(n):
    return lambda x: x % n > 0

def primes():
    yield 2

    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_dividable(n), it)

for i in primes():
    if i < 20:
        print(i)
    else:
        break

# 回数
# 回数是指从左向右读和从右向左读都是一样的数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_palindrome2(n):
    return lambda x: str(x) == str(x)[::-1]

output = filter(is_palindrome, range(10, 60))
output2 = filter(is_palindrome2(0), range(10, 60))
print('10~60:', list(output), list(output2))

print('#'*10, '4.filter', 'start' if 0 else 'end', '#'*10)

# 5.sorted
# 参数key指定的函数将作用于list的每一个元素上(不改变原始值)，并根据key函数返回的结果进行排序。
print('#'*10, '5.sorted', 'start' if 1 else 'end', '#'*10)
print(sorted([-5, 8, 0, -32, 99]))
print(sorted([-5, 8, 0, -32, 99], key = abs))
print(sorted([-5, 8, 0, -32, 99], key = lambda x: x if x >= 0 else -x, reverse = True))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))

L5 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t): return t[0]
def by_score(t): return -t[1]
print(sorted(L5, key = by_name), sorted(L5, key = by_score))
print('#'*10, '5.sorted', 'start' if 0 else 'end', '#'*10)

# 6.返回函数
''' 复习函数参数开始
  # 位置参数：power(x, n) 函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
  # 默认参数：power(x, n=2) 1.必选参数在前，默认参数在后；2.当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数；
             3.有多个默认参数时，调用的时候，既可以按顺序提供默认参数，也可以不按顺序提供部分默认参数，当不按顺序提供部分默认参数时，需要把参数名写上；
             4.定义默认参数要牢记一点：默认参数必须指向不变对象！
  # 可变参数：calc(*numbers) 定义可变参数需要在参数前面加一个*号，这些可变参数在函数调用时自动组装为一个tuple，可以传入任意个参数，包括0个参数。
             nums=[1,2,3] or nums=(1,2,3),  calc(*nums) *nums表示把nums这个list的所有元素作为可变参数传进去。
  # 关键字参数：person(name, age, **kw) 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
               1.函数person除了必选参数name和age外，还接受关键字参数kw，在调用该函数时，可以只传入必选参数；
               2.也可以传入任意个数的关键字参数，如person('Adam', 45, gender='M', job='Engineer')；
               3.和可变参数类似，也可以先组装出一个dict，如extra = {'city': 'Beijing', 'job': 'Engineer'}，然后，把该dict转换为关键字参数传进去，
                 如person('Jack', 24, city = extra['city'])；也可以person('Jack', 24, **extra)，**extra表示把extra这个dict的所有key-value
                 用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
  # 命名关键字参数：1.对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，至于到底传入了哪些，就需要在函数内部通过kw检查。
                   如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数，这种方式定义的函数如下：person(name, age, *, city, job)
                   和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
                   2.如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：person(name, age, *args, city, job),
                     命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错;命名关键字参数可以有缺省值，从而简化调用
  # 参数组合：在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，
             参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数，
             所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
             虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。               
'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args2 = (1, 2, 3)
kw2 = {'d': 88, 'x': '#'}
f2(*args2, **kw2)
''' 复习函数参数结束'''

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
print('#'*10, '6.返回函数', 'start' if 1 else 'end', '#'*10)
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种程序结构称为“闭包(Closure)。
# 返回的函数并没有立刻执行，而是直到调用了f()才执行。
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

f3 = lazy_sum(1,3,5,7,9)
f4 = lazy_sum(1,3,5,7,9)
print(f3, f4(), f3 == f4)
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变。
# count2()缺点是代码较长，可利用lambda函数缩短代码。
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f4, f5, f6 = count2()
print(f4(), f5(), f6())
# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    i = 0
    def counter():
        nonlocal i
        i += 1
        return i
    return counter

def  createCounter2():
    l = [0]
    def counter():
        l[0] += 1
        return l[0]
    return counter

def  createCounter3():
    def g():
        n = 1
        while True:
            yield n
            n += 1

    f = g()
    def counter():
        return next(f)

    return counter

counterA = createCounter3()
print(counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter3()
print(counterB(), counterB(), counterB(), counterB())
print('#'*10, '6.返回函数', 'start' if 0 else 'end', '#'*10)

# 7.匿名函数
# 关键字lambda表示匿名函数。匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
print('#'*10, '7.匿名函数', 'start' if 1 else 'end', '#'*10)
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(list(filter(lambda n: n % 2 == 1, range(1, 20))))
def g_lambda(a, b, f): return f(a, b)
print(g_lambda(2, 2, lambda x,y: 'equal' if x == y else 'no'))
print('#'*10, '7.匿名函数', 'start' if 0 else 'end', '#'*10)

# 8.装饰器
import functools
# 在代码运行期间动态增加功能的方式，称之为“装饰器”(ecorator)。本质上，decorator就是一个返回函数的高阶函数。
print('#'*10, '8.装饰器', 'start' if 1 else 'end', '#'*10)
# e.g. 1
def log(func):
    print('log start')
    #经过decorator装饰之后的函数，它们的__name__已经从原来的名字(如接下来的'now')变成了'wrapper'，加上下面这句可以阻止该动作
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s start:' % func.__name__)
        func(*args, **kw)
        print('call %s end:' % func.__name__)
    print('log end')
    return wrapper

#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
    print('20190724-152535')

print(now.__name__) #测试@functools.wraps(func)
now() #注意观察print顺序
print(now.__name__)

# e.g. 2
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s:' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 相当于执行了语句：now2 = log('execute')(now2)
@log2('execute')
def now2():
    print('20190724-165516')

print(now2.__name__)
now2()
print(now2.__name__)

# e.g. 3
# 这种情况下首先 E(str) = C(E)(str)，然后由于C = A(C)，还有 E(str) = A(C)(E)(str)。
# 这么一来他们的关系就明确了，装饰器 A 装饰的是装饰器 C，它返回了一个被装饰过的装饰器，
# 而被装饰过的装饰器又可以去装饰函数 E。在上面的代码中，decorated_C 就是一个被装饰过的装饰器。

def A(funC):
    def decorated_C(funE):
        def decorated_E_by_CA(*args, **kwargs):
            out = funC(funE)(*args, **kwargs)
            return out +' > decorated by A'
        return decorated_E_by_CA
    return decorated_C

@A
def C(funE):
    def decorated_E_by_C(str):
        return funE(str)+' > decorated by C'
    return decorated_E_by_C

@C
def E(str):
    return str

print(E.__name__)
print(E('E string is '))
print(E.__name__)

# e.g. 4
# 这种情况下，有 E2(str) = A2(C2(E2))(str)。首先装饰器 C2 装饰函数 E2，返回一个被 C2 装饰过的函数，
# 然后装饰器 A2 再装饰这个被 C2 装饰过的函数。与第一种情况的区别是，这里的装饰器 A2 装饰的是一个函数，而不是一个装饰器。
def A2(funE2_decorated_by_C2):
    def redecorated_E2(str):
        return funE2_decorated_by_C2(str)+' > redecorated by A2'
    return redecorated_E2

def C2(funE2):
    def decorated_E2(str):
        return funE2(str)+' > decorated by C2'
    return decorated_E2

@A2
@C2
def E2(str):
    return str

print(E2.__name__)
print(E2('E2 string is ')) #等价于print(A2(C2(E2))('E2 string is '))，此时E2不加装饰器
print(E2.__name__)

print('#'*10, '8.装饰器', 'start' if 0 else 'end', '#'*10)