#pow(x, y, z=None, /)
#    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)

#x**y
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2, 3))


def calc(numbers):
    sum = 0
    for n in numbers:
        print(n,end=" ")
        sum = sum + n * n
    return sum


sum = calc(range(10))
print(sum)

#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
print(calc(*nums))
sum1 = calc(1, 2, 3, 4, 5, 5, 4)
print(sum1)


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

# 命名关键字参数
def person1(name, age, *, city, job):
    print(name, age, city, job)

def person2(name, age, *args, city, job):
    print(name, age, args, city, job)

def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)

#person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
person('Jack', 24, city='Beijing', job='Engineer',addr='Chaoyang', zipcode=123456)
person1('Jack', 24, city='Beijing', job='Engineer1')
#person1('Jack', 24, city='Beijing', job='Engineer',addr='Chaoyang', zipcode=123456)
#person1('Jack', 24, 'Beijing', 'Engineer')
# TypeError: person1() takes 2 positional arguments but 4 were given
person2('Jack2', 24,city='Beijing', job='Engineer2')
#person2('Jack', 24, city='Beijing', job='Engineer2',addr='Chaoyang', zipcode=123456)
person3('Jack3', 24, job='Engineer3')


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3,4,5)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
f2(*args, **kw)