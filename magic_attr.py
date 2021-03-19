class C:
    def __getattribute__(self, name):       #定义当该类的属性被访问时的行为
        print("getattribute")
        return super().__getattribute__(name)

    def __getattr__(self, name):            #定义当用户试图获取一个不存在的属性时的行为
        print("getattr")

    def __setattr__(self, name, value):     #定义当一个属性被设置时的行为
        print("setattr")
        return super().__setattr__(name,value)

    def __delattr__(self, name):            #定义当一个属性被删除时的行为
        print("delattr")
        super().__delattr__(name)

c = C()
c.x
c.x = 1
c.x
del c.x