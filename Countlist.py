class Countlist:
    def __init__(self,*args):
        self.vaule = [x for x in args]
        self.count = {}.fromkeys(range(len(self.vaule)),0)

    def __len__(self):                  #定义当被 len() 调用时的行为（返回容器中元素的个数）
        return len(self.vaule)

    def __getitem__(self, key):         #定义获取容器中指定元素的行为，相当于 self[key]
        self.count[key] +=1
        return self.vaule[key]


#，容器类型：不可变列表，统计每个index的访问次数
print(help({}.fromkeys))
#fromkeys(iterable, value=None, /) method of builtins.type instance
#    Create a new dictionary with keys from iterable and values set to value.
c1 = Countlist(1,3,5,7,9)
print(c1.vaule)
print(len(c1.vaule))
print(c1[0])
print(c1[2])
print(c1.count)
print(c1.__dict__)

c2 = Countlist(2,4,6,8,10,12)
print(c2.__dict__)
print(c1[0] + c2[1])
print(c1.count)
print(c2.count)

