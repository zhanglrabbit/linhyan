class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()


print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

#getattr(obj, 'z') # 获取属性'z'
g = getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
print(g)

print(hasattr(obj, 'power'))
#print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())

