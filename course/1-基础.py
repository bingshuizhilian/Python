#name=input("please enter a name\n")

#print('hello', name)

r'''1
a = -100 ;b=200;c=0

if(a>0):
    print(a)
    print(b)
    print('中文A')
elif c ==0 :
    print('a!=0')
else:
 print(-a)
 print(-b)
 print('中文B')
 '''

r'''2
sum = 0
for i in range(1,100):
    sum += i
     
print(sum)

sum=0 ;n=99
while n>0:
    sum+=n
    n-=2
print(sum)

#web 函数
'''

def func1(param1, param2 = 5):
    if not isinstance(param1, (int, float)):
        raise TypeError('param1类型错误')
    elif not isinstance(param2, (int)):
        raise TypeError('param2类型错误')
    m = 10;
    if param1 >= 10:
        m = param1;
    elif param2 >= 10:
        m=param2
    else:
        m=-1

    return(m)

def nop():
    pass

#range([start,]end[,step]) 从start开始，到stop结束（不包括stop），步长为step
for i in range(9,-1,-1):
    print (i)

for i in range(9,0,-1):
    print (i)

import math
def quadratic(a,b,c):
    
    if not isinstance(a,(int,float)):
        raise TypeError('a type error')
    elif not isinstance(b,(int,float)):
        raise TypeError('b type error')
    elif not isinstance(c,(int,float)):
        raise TypeError('c type error')

    if(b*b-4*a*c < 0):
        raise ValueError(b*b-4*a*c)

    return (-b+math.sqrt(b*b-4*a*c))/2/a, (-b-math.sqrt(b*b-4*a*c))/2/a

L=[1,2,3]
def calc(n):
    sum=0
    for i in n:
        sum += i**2
    return sum

def calc2(*n):
    sum=0
    for i in n:
        sum += i**2
    return sum

calc(L)
calc2(*L)
dict1 = {'mike':14, 'bob':56, 'lily':17, '13':13}

for k in dict1:
    print(k)

for v in dict1.values():
    print(v)

for k,v in dict1.items():
    print(k,v)
    

def person(name, age, **kws):
    print('name:',name,'age:',age,'others:',kws)
    if 'lily' in kws:
        print('lily is here')

person('lily', 16, city='newyork')
person('lucy', 17, **dict1)

def person2(name, age, *, city, job):
    print('name:',name,'age:',age,'city:',city,'job:',job)

person2('lily', 16, city='newyork', job='stu')

def person3(name, age, *others, city='harbin', job):
    print('name:',name,'age:',age,'others:',others,'city:',city,'job:',job)

person3('lily', 16, [1,2],city='newyork', job='stu')

person3('lily',16,{'grade':3},job='stu')


def product(*L):
    if len(L) == 0:
        raise TypeError('L is empty')
    else:
        multi = 1
        
    for i in L:
        multi *= i
        
    return multi

try:
    product()
    print('failed')
except TypeError:
    print('succ')

def temp(a,b,c):
    print(a+b+c)

def fact(n):
    if n == 1:
        return 1;

    return n*fact(n-1)

#递归
def hanoi(n,a,b,c):
    if 1 == n:
        print('move', a, '-->', c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)
        
def myprint():
    temp(1,2,3)
    temp(*(1,2,3))
    temp(**{'a':1,'b':2,'c':3})
    print(fact(100))
    hanoi(4,'a','b','c')

myprint()

#切片
L1=['mike','lily','david','john','tim','sarah','jack','89',13]

L1[:4]
L1[0:4]
L1[4:6]
L1[-3:]
L1[-4:-1]
L1[:5:2]
L1[::3]
'ABCDEFGHIJK'[:3]
'ABCDEFGHIJK'[::3]
(0, 1, 2, 3, 4, 5)[:3]

str = '   hello  world   '

def trimC(s):
    if 0 == len(s):
        return s
    
    f=True
    for t in s:
        if t != ' ':
            f=False

    if f:
        return ''

    for i in range(0,len(s)):
        if s[i] != ' ':
            s = s[i:]
            break
    
    for i in range(len(s)-1,-1,-1):
        if s[i] != ' ':
            s = s[:i+1]
            break
    
    return s

def trimP(s):
    while s[:1] == ' ':
        s = s[1:]
        
    while s[-1:] == ' ':
        s = s[:-1]
        
    return s
    
    
print('trimC:', trimC(str))
print('trimP:', trimP(str))


from collections import Iterable

print(isinstance('abc', Iterable))

for i,v in enumerate(['a', 'b', 'c']):
    print(i,v)

for i,v in [(1,2), (2,4), (3,9), (9,'a')]:
    print(i,v)

for i,v in enumerate([(1,2), (2,4), (3,9)]):
    print(i,v)

def findMinAndMax(L):
    a,b = None,None
    
    if [] == L:
        return (a,b)

    a=L[0];b=L[0]
    for i in L:
        if i<a:
            a=i

    for j in L:
        if j > b:
            b=j

    return (a,b)

