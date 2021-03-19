class New_int(int):
    def __add__(self, other):
        return int.__sub__(self, other)

    def __sub__(self, other):
        return int.__add__(self, other)


a = New_int(2)
b = New_int(8)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)


class Try_int(int):  # 默认继承int
    def __add__(self, other):
        # return  self + other        #返回对象+对象 重新触发 __add__  ，死循环
        return int(self) + int(other)

    def __sub__(self, other):
        return int(self) - int(other)


c = Try_int(1)
d = Try_int(2)
print(c + d)
print(c - d)
print(c ** d)
print(c / d)
print(c % d)


'''>>> str.__new__.__doc__ 
'Create and return a new object.  See help(type) for accurate signature.' '''


