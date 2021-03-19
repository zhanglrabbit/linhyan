class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):    #定义当一个属性被设置时的行为
        if name == 'square':
            self.width = value
            self.height = value
        else:
            #self.name = value      #实例属性赋值  __setattr__ 属性方法死循环
            #super().__setattr__(name,value)
            self.__dict__[name] = value

    def getArea(self):
        return self.width * self.height


#from Rectangle import *
r = Rectangle(3,5)
print(r.__dict__)
print(r.getArea())
r.square = 10
print(r.width)
print(r.height)
print(r.getArea())
print(r.__dict__)
r1 = Rectangle(2,5)
r1.ab = 8
print(r1.__dict__)
print(r1.getArea())

