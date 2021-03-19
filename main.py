import Exception_practice
Exception_practice.test()
print(Exception_practice.__doc__)
print(Exception_practice.__author__)

import greeting
t1 = greeting.greeting('linhuiyan')
t2 = greeting._private_1('lin')
t3 = greeting._private_2('yan')
t4 = greeting.greeting('lin')
print(t1)
print(type(t1))
print(dir(t1))
print(t2)
print(t3)
print(t4)

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


print_score(std1)


import func_str2float

f1 = func_str2float
print(type(f1))




def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f())
    return fs


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


