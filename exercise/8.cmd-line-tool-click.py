#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：8.cmd-line-tool-click.py '

__author__ = 'bingshuizhilian'



import click

'''
参考链接：https://blog.csdn.net/u010339879/article/details/80542099

click模块可以轻松将一个函数变成一个命令行工具
'''

# 1. click是基于装饰器的，我们可以在方法上使用click.command()装饰器来将该方法变成一个命令行工具
@click.command()
def fun():
    click.echo('Hello World!')

'''
2 click.option
option 最基本的用法就是通过指定命令行选项的名称，从命令行读取参数值，再将其传递给函数。我们除了设置命令行选项的名称，
我们还会指定默认值，help 说明等，option 常用的设置参数如下：

default: 设置命令行参数的默认值
help: 参数说明
type: 参数类型，可以是 str, int, float 等
prompt: 当在命令行中没有输入相应的参数时，会根据 prompt 提示用户输入可以指定 True, 或者特定字符串来提示用户输入
nargs: 指定命令行参数接收的值的个数, -1 表示可以接收多个参数
'''
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def fun2(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    '''usage: $python xxx.py --name frank --count 3'''
    for i in range(count):
        click.echo('Hello %s!' % name)

@click.command()
@click.option('--rate', '-rate', '-r', type=int, help='rate')
def fun3(rate):
    print(f'type(rate):{type(rate)}')
    click.echo('rate: %s!' % rate)

@click.command()
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
def fun4(hash_type):
    print('hash_type:{}'.format(hash_type))




if __name__ == "__main__":
    # fun()
    # fun2()
    # fun3()
    fun4()
