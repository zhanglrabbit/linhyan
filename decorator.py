# -*- coding: utf-8 -*-
import time, functools


def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;




@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11,22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


f2 = fast
t1 = type(f2)
d1 = dir(fast)
print(d1)
print(t1)
print(f2(11,27))
