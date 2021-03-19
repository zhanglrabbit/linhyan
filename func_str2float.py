# -*- coding: utf-8 -*-
from functools import reduce
'''第三题基本思路：
1. 找到小数点的位置
2. 将原来的字符串去掉小数点
3. 先通过 map 将字符串转为 float
4. 通过 reduce 将字符串转为整数
5. 最后通过小数点的位置乘上 10 -n 次幂'''
def str2float(s):
    spl = s.split('.',1)
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    def fn(x, y):
        return x * 10 + y
    def fun(a, b):
        zheng = reduce(fn,map(char2num,a))
        xiao = reduce(fn,map(char2num,b))
        return zheng + xiao / 10 ** len(b)
    return fun(spl[0],spl[1])
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
