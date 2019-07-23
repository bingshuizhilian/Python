# -*- coding: utf-8 -*-

# 传入函数/高阶函数
def add(a, b, f):
        return f(a) + f(b)

print(add(-6, 9, abs))