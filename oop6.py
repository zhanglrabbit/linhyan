class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('zhangl')
s.score = 90
print(s.score)
print(s.name)

