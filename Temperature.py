class Celsius:
    def __init__(self,value=26.0):
        self.value = float(value)

    def __get__(self, instance, owner):         # 定义当描述符的值被取得时的行为
        return self.value

    def __set__(self, instance, value):         # 定义当描述符的值被改变时的行为
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel*1.8  + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) /1.8     #赋值行为，调用Celsius__set__

class Temperature:
    cel = Celsius()             # 描述符就是将某种特殊类型的类的实例指派给另一个类(被描述)的属性
    fah = Fahrenheit()          # 描述符就是将某种特殊类型的类的实例指派给另一个类(被描述)的属性


temp = Temperature()
temp.cel = 30
print(temp.__dict__)
print(temp.fah)

temp2 = Temperature()
temp2.fah = 100
print(temp2.__dict__)
print(temp2.cel)

print(__name__)
print(dir())
