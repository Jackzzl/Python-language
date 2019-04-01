# /usr/bin/env Python3
# -*- encoding:UTF-8 -*-
# test.py

import functools


def decoretor(func):
    @functools.wraps(func)  # 注意，我们最后还是要验证run还是不是run
    def my_run():  # 扩展run，在跑之前喊 预备，跑完之后，告知比赛结束
        print('预备................')
        f = func  # 我们最后返回这个func ，实际上也可以不这样写，直接 return func就行，这里为了展示效果
        func()  # 这里我们开始 跑，实际上执行的是函数run
        print('比赛结束............')
        return f  # 返回 f -- func函数的副本，这里返回的是run函数的副本，功能一模一样，但是但是函数对象的地址不一样

    return my_run  # 返回我们的装饰器（扩展函数）


@decoretor
def run():
    print('跑')  # 装饰器作用的对象是run这个函数


f = run()  # 因此，我们执行run函数的同时，我们的装饰器也没闲着，扩展功能将作用在run运行前后
print(run)  # 打印run函数对象的内存地址
print(f)  # 装饰器返回的是一个函数，而这个函数的返回值又是一个函数，这个函数是run函数的功能属性拷贝函数，不==run
print(f.__name__)  # 无论有没有@functools.wraps(func)限制，这个f始终是run，也就是run的副本
print(run.__name__)  # run是不是run还要看@functools.wraps(func)这行代码
f()  # 我们运行一下run函数的副本