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
print('#'*10, '5.sorted', 'start' if 1 else 'end', '#'*10)


print('#'*10, '5.sorted', 'start' if 0 else 'end', '#'*10)
