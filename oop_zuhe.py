class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, y):
        self.num = y


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        #print('水池里有乌龟%d只,小鱼 %d 条！' % (self.turtle, self.fish))
        print('水池里有乌龟%d只,小鱼 %d 条！' % (self.turtle.num, self.fish.num))


p = Pool(2,3)
p.print_num()

'''>>> str.__new__.__doc__ 
'Create and return a new object.  See help(type) for accurate signature.'  '''

#str.upper.__doc__
#'S.upper() -> str\n\nReturn a copy of S converted to uppercase.'

class Capstr(str):
    def __new__(cls, string):   #string  不可变字符串对象，通过__new__重写
    #def __new__(cls, *args, **kwargs):
        string = string.upper()
        return str.__new__(cls,string)   #调用默认str __new__

a = Capstr("I love fishc.com!")
print(a)