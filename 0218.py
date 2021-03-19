import functools
def log(temp):
    if not isinstance(temp,str):
        #使用decorator后,func指向log(func)
        #将更名后的'__name__'更改回原函数名称防止签名错误
        @functools.wraps(temp)
        def wrapper(*args,**kw):
            ##operations
            return temp(*args,**kw)
        return wrapper
    else: #此时temp为一串str参数
        #new decorator
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print(temp) #打印字符串temp
                #operations
                return func(*args,**kw)
            return wrapper
        return decorator

#即支持
@log
def f():
    pass
#又支持
@log('hello world')
def f1():
    pass

@log('linhyan')
def f2():
    pass

@log
def plus(x,y):
    print(x + y)

p0 = plus(2,5)
print(p0)

@log('linhyan')
def plus(x,y):
    print(x + y)

p1 = plus(2,5)
print(p1)






f()
print(f.__name__)
print(dir(f))
print(type(dir(f1)))
f1()
print(f1.__name__)
print(dir(f1))
print(type(dir(f1)))
f2()
print(f2.__name__)
print(dir(f2))
print(type(dir(f2)))