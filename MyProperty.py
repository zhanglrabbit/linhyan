class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):  # 定义当描述符的值被取得时的行为
        return self.fget(instance)

    def __set__(self, instance, value):  # 定义当描述符的值被改变时的行为
        self.fset(instance, value)

    def __delete__(self, instance):  # 定义当描述符的值被删除时的行为
        self.fdel(instance)


class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = MyProperty(getX, setX, delX)  # 描述符就是将某种特殊类型的类的实例指派给另一个类(被描述)的属性


c = C()
c.x = 'x-man'
c.x
c._x
