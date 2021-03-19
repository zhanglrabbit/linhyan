# -*- coding: utf-8 -*-
import math
def quadratic(a, b, c):
    for t in (a,b,c): 
        if not isinstance(t,(int,float)):
            raise TypeError('bad operand type')
    if b*b-4*a*c < 0:
        return ('此方程组无解')
    else:
        x1 = ((-b+math.sqrt(b*b-4*a*c))/(2*a))
        x2 = ((-b-math.sqrt(b*b-4*a*c))/(2*a))
        #return(print('%.2f ,%.2f' %(x1,x2)))
        return x1, x2
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')	
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
nums.append(4)
calc(*nums)
# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
extra = {'city': 'Beijing', 'job': 'Engineer'}
extra['sex']='man'
person('Jack', 24, **extra)
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
args = ('a','b','c')
kw = {'d':1000 , 'x': '#','y':100}
f1(1,2,3,4,5,5,x = 1,y=2,z=3)
f1(*args, **kw)
f2(*args, **kw)
def product(*numbers):
    a=1
    if not isinstance(numbers,int and float and list and tuple ):
        raise TypeError('请输入一个或多个整数或小数')
    elif len(numbers)<0:
        return '请输入一个或多个数'
    for n in numbers:
        a=a*n
    return a
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
# do_slice
def trim(s):
    if not isinstance(s,str):
        raise TypeError('请输入一个list或字符串')
    if len(s) == 0:
        return s
    elif s[0]==" " and len(s)>0 :
        s=trim(s[1:])
    elif s[-1]==" " and len(s)>0 :
        s=trim(s[:-1])
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
# findMinAndMax
def findMinAndMax(L):
    if L == []:
        return(None,None)
    max=L[0]
    min=L[-1]
    for x in L:
        while x > max:
            max = x
        while x < min:
            min = x
    return(min,max)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
# 列表推导式
L1 = ['Hello', 'World', 18, 'Apple', None]
#保留数字
L2 = [x.lower() if isinstance(x,str)==True else x for x in L1 if x!=None]
print(L2)
#只要字符串
L2 = [x.lower() for x in L1 if isinstance(x,str)==True]
print(L2)
