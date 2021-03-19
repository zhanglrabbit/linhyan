def f(x):
    return x * x

#'map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。'
#'map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。'


print(f(10))
a = 5
print(f(a))

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(r))
l = list(r)
print(type(l))
print(l)

s = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(s)
