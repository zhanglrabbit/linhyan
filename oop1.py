class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(60)  # ok!
re1 = s.get_score()
print(type(re1))
print(re1)
# s.set_score(600)
# s.set_score('aa')
