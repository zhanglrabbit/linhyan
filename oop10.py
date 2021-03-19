class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
#s.score = 99 # 绑定属性'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999