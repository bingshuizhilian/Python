#!/usr/bin/env python3            # 此注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-           # 此注释表示.py文件本身使用标准UTF-8编码

' module using example '          # 此字符串表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
                                  # 可以用特殊变量__doc__访问此文档注释

__author__ = 'bingshuizhilian'    # 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以知道作者信息

# 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。


import sys



### 1.使用模块
# 在Python中，一个.py文件就称之为一个模块(Module)
# 为了避免模块名相同的冲突，Python引入了按目录来组织模块的方法，称为包(Package)。
# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符。
# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc。
'''1.单级包
mycompany        ：顶层包名
├─ __init__.py   ：每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，
|                  而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany
├─ abc.py        ：现在，abc.py模块的名字就变成了mycompany.abc
└─ xyz.py
'''

'''2.多级包
mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py       # mycompany.web.utils
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py          # mycompany.utils
'''
print('#'*10, '1.使用模块', 'start' if 1 else 'end', '#'*10)
def moduleTest():
    # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    args = sys.argv
    print(args)

# 当我们在命令行运行某模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该模块时，
# if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
    moduleTest()

# 在命令行执行python 4-模块.py 12 hello 0x23 'world' "!"
# 命令行回显：['4-模块.py' '12' 'hello' '0x23' "'world'" '!']
print('#'*10, '1.使用模块', 'start' if 0 else 'end', '#'*10)



### 2.作用域
'''
1.在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，
  有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
2.正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等。
3.类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等。
  之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有
  一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
'''
print('#'*10, '2.作用域', 'start' if 1 else 'end', '#'*10)
print('__doc__:', __doc__)
print('#'*10, '2.作用域', 'start' if 0 else 'end', '#'*10)



### 3.安装第三方模块
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索。
# 用pip安装费时费力，还需要考虑兼容性。推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库。
print('#'*10, '3.安装第三方模块', 'start' if 1 else 'end', '#'*10)
print('https://pypi.org/')
print('https://www.anaconda.com/')
print('#'*10, '3.安装第三方模块', 'start' if 0 else 'end', '#'*10)



### 4.模块搜索路径
'''
当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错，
默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在
sys模块的path变量中，如果我们要添加自己的搜索目录，有两种方法：
一、直接修改sys.path，添加要搜索的目录：sys.path.append('/Users/michael/my_py_scripts')
    这种方法是在运行时修改，运行结束后失效。
二、设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path
    环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
'''
print('#'*10, '4.模块搜索路径', 'start' if 1 else 'end', '#'*10)
print(sys.path)
sys.path.append('C:/Users/Administrator/Desktop')
print(sys.path)
print('#'*10, '4.模块搜索路径', 'start' if 0 else 'end', '#'*10)
