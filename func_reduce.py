from functools import reduce
def add(x,y):
    return  x + y

h = help(reduce)
print(h)
print(reduce.__doc__)
r = reduce(add, [1, 3, 5, 7, 9])
t = type(r)
l1 = [1, 3, 5, 7, 9]
sum(l1)
print(r)
print(t)
