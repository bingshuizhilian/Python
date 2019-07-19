#列表生成式
import os
dict2 = {'x': 'A', 'y': 'B', 'z': 'C' }
L2 = ['Hello', 'World', 'IBM', 'Apple']
L3 = ['Hello', 'World', 68, 'IBM', 'Apple', None]

l1=list(range(1,11))
l2=[x*x for x in range(1,11) if x%2==0]
l3=list(x*x for x in range(1,11) if x%2==0 and x!=6)
l4=[m+n for m in 'ABC' for n in '0123']
l5=[d for d in os.listdir()]
l6=[k+'='+v for k,v in dict2.items()]
l7=[s.lower() for s in L2]
l8=[s.lower() for s in L3 if isinstance(s, str)]

for i in range(1,9):
    exec('print(l{})'.format(i))

print('{0}'.format(l1))



#生成器
g = (x*x for x in range(1,11))

print('g', '*'*20)
for i in g:
    print(i)


def foo():
    print("starting1...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print("*"*20)
print(g.send(7))

def foo2(num):
    print("starting2...")
    while num<10:
        num=num+1
        yield num

g2=foo2(3)
print('g2', '*'*20)
for n in g2:
    print(n)


def fib(num):
    n,a,b=0,0,1
    while n<num:
        yield b
        n,a,b=n+1,b,a+b

    return 'done'

g3=fib(6)
print('g3', '*'*20)
while True:
    try:
        x=next(g3)
        print(x)
    except StopIteration as e:
        print(e.value)
        break


def triangles():
    L=[1]
    
    while True:
        yield L
        L=[1] + [L[x] + L[x+1] for x in range(len(L) - 1)] + [1]

def triangles2():
    L = [1]
        
    while True:
        yield L
        
        K=[]
        for n in range(len(L) - 1):
            K += [L[n] + L[n+1]]

        L = [1] + K + [1]

        
g4=triangles()
print('g4', '*'*20)
n=0
for c in g4:
    print(c)
    if n == 9:
        break
    n+=1



#迭代器
from collections import Iterable
from collections import Iterator

print(isinstance((x for x in range(10)), Iterable),
isinstance((x for x in range(10)), Iterator),
isinstance(iter('abc'), Iterator))


