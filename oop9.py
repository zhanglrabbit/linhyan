class Student(object):
    pass
    # __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


def set_score(self, score):
    self.score = score


Student.set_score = set_score

s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性(变量)
print(s.name)


# print(Student.name)
def set_age(self, age):  # 定义一个函数作为实例方法（函数）
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(dir(s))
print(s.age)
a = s.set_score(100)
print(type(a))
print(s.score)
# help(MethodType)


s2 = Student()  # 创建新的实例
print(dir(s2))
s2.set_score(100)
print(s2.score)
# print(dir(object))
# s2.set_age(25) # 尝试调用方法
