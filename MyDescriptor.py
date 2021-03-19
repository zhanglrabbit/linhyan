class MyDescriptor:
    def __get__(self, instance, owner):  # 定义当描述符的值被取得时的行为
        print("getting...", self, instance, owner)

    def __set__(self, instance, value):  # 定义当描述符的值被改变时的行为
        print("setting...", self, instance, value)

    def __delete__(self, instance):  # 定义当描述符的值被删除时的行为
        print("deleting...", self, instance)


class Test:
    x = MyDescriptor()  # 描述符就是将某种特殊类型的类的实例指派给另一个类(被描述)的属性


test = Test()
test.x
test
Test
test.x = "x-man"
del test.x
