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
click.option
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

# 指定type
# 可以通过--, 或 - 来传递参数
@click.command()
@click.option('--rate', '-rate', '-r', type=int, help='rate')
def fun3(rate):
    print(f'type(rate):{type(rate)}')
    click.echo('rate: %s!' % rate)

# type可以设定可选值
@click.command()
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
def fun4(hash_type):
    print('hash_type:{}'.format(hash_type))

# 需要输入密码, 可以用option
@click.command()
@click.option('--password', '-p', prompt=True, hide_input=True, confirmation_prompt=True)
def fun5(password):
    click.echo('password: %s' % password)

# 输入密码有一个专门的装饰器click.password_option()
@click.command()
@click.password_option()
def fun6(password):
    click.echo('password: %s' % password)

'''
click.argument
除了使用 @click.option 来添加可选参数，还会经常使用 @click.argument 来添加固定参数。它的使用和 option 类似，但支持的功能比 option 少
'''
# 为命令行添加固定参数(固定参数不需要在前面加--或-)
# e.g. $python xxx.py lily
@click.command()
@click.argument('name')
@click.argument('age')  # 多个argument需要写成多行，不能在一个argument里传多个参数
def fun7(name, age):
    click.echo('Hello %s, %s' % (name, age))

'''
!!!!!!!!!!!!!!!!!!!!!!!这个功能非常实用!!!!!!!!!!!!!!!!!!!!!!!
nargs的用法,可以吸收多余的参数
# 其中，nargs=-1 表明参数 src 接收不定量的参数值，参数值会以 tuple 的形式传入函数。
# 如果 nargs 大于等于 1，表示接收 nargs 个参数值，上面的例子中，dst 接收一个参数值。
# The value is then passed as a tuple. Note that only one argument can be set to nargs=-1, as it will eat up all arguments.
# 用来吸收多余的参数, 作为一个元组传值
'''
@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)  # 这两个需要配合使用，单独只写第一行来表示多参数经验证不可行
def fun8(src, dst):
    click.echo('move %s to %s' % (src, dst))
    click.echo(src[0])

# 嵌套命令
# 可以通过group来实现命令行的嵌套，也就是让一个命令行工具具有多个命令
# e.g. $python xxx.py initdb 20191106
@click.group() 
def fun9():
    click.echo('Hello world')

@fun9.command()
@click.argument('date')
def initdb(date):
    click.echo('Initialized the database %s' % date)

@fun9.command()
@click.argument('args1', nargs=-1)
@click.argument('args2', nargs=1)
def dropdb(args1, args2):
    click.echo('Dropped the database %s, %s' % (args1, args2))

if __name__ == "__main__":
    # fun()
    # fun2()
    # fun3()
    # fun4()
    # fun5()
    # fun6()
    # fun7()
    # fun8()
    fun9()
