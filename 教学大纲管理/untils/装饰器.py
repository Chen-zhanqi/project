# -*- coding: utf-8 -*-
__author__ = 'wj'
__date__ = '2018/10/29 14:16'

# 语法糖
# 装饰器原理就是使用闭包来实现的
# 闭包：
# 1.函数嵌套函数
# 2.内部函数使用外部函数的变量
# 3.外部函数返回的是内部函数对象


def test(number):

    # number是一个局部变量
    def sum(num2):

        return number * num2

    return sum

# sum 就是test函数执行完成后返回的结果，返回的就是test函数内部的sum函数对象
#
sum = test(10)
# sum是一个函数对象，如果想要执行必须得调用，调用完成后就是执行了test内部的sum函数
# 如果sum想要执行，必须先执行test外部函数，一般我们称内部的sum函数为闭包
rs = sum(20)
print(rs)

from datetime import datetime
from functools import wraps


# 不带参数的装饰器
# 计算函数运行时间的装饰器
def run_time(func):
    # @wraps 保留原有的func函数的结构和文档
    @wraps(func)
    def _func():

        start = datetime.now()
        func()
        print(datetime.now() - start)

    return _func

@run_time
def for10000_test():
    """
    这是原来的for10000_test函数
    :return:
    """
    for x in range(10000):
        print(x)

print(for10000_test.__doc__)

# @run_time 等同于以下的操作
# 执行rum_time 将for10000_test传入函数中，接收外部函数返回值
# _func = run_time(for10000_test)
# 将_func函数赋值给for10000_test变量
# for10000_test = _func
# 调用for10000_test，相当于调用了_func
# for10000_test()

# 权限装饰器
def permission(func):

    @wraps(func)
    def _func(*args, **kwargs):

        return func(*args, **kwargs)

    return _func


# 函数带参数的装饰器
@permission
def subject_list(request):


    return 'response'

result = subject_list('request', '1', 2, 3)
































