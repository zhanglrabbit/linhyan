class Student(object):

    @property    #装饰器就是负责把一个方法变成属性调用的：
    def score(self):
        return self._score

    @score.setter   #@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
s.score # OK，实际转化为s.get_score()
#s.score = 9999



class Student1(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):      #定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
        return 2015 - self._birth

s1 = Student1()
s1.birth = 1988
print(s1.birth)
print(s1.age)
