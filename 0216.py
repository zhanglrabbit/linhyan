# -*- coding: utf-8 -*-
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print ('begin call')
        s = func(*args,**kw)
        print('end call')
        return s
    return wrapper

@log
def plus(x,y):
    print(x + y)

plus(2,5)