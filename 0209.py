#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


#如果是str就是有参数的decorator
#如果是function就是没有参数的decorator（无参会传入被装饰函数）


def log(test):
    if isinstance(test, str):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print('log of %s:%s' % (fn.__name__, test))
                return fn(*args, **kw)


            return wrapper

        return decorator
    else:
        @functools.wraps(test)
        def wrapper(*args, **kw):
            print('log of %s:%s' % (test.__name__, 'defult'))
            return test(*args, **kw)

        return wrapper


# 测试
@log('test')
def f(x, y):
    return x + y


f(1, 2)


@log
def fn(x, y):
    return x * y


fn(1, 2)
