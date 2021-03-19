class Fibs:
    def __init__(self, n=10):
        self.a = 0
        self.b = 1
        self.n = n
        #容器是用来储存元素的一种数据结构，容器将所有数据保存在内存中，Python中典型的容器有：list，set，dict，str等等
    def __iter__(self):             #定义当迭代容器中的元素的行为
        return self

    def __next__(self):
        self.a,self.b =  self.b,self.a +self.b
        #self.a = self.b
        #self.b = self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


fibs = Fibs()
print(fibs.__next__())
print(next(fibs))
print(next(fibs))
print(next(fibs))
print()
for each in fibs:
    print(each, end=" ")
print()
print(fibs.__dict__)
print(fibs.__iter__())
#print(fibs.__next__())
print(fibs)
print()
fibs1 = Fibs(1000)
print(fibs1.__dict__)
for each in fibs1:
    print(each, end=" ")

print(iter.__doc__)
print(next.__doc__)
string ="linhyan"
it = iter(string)
print(next(it))
print(next(it))


