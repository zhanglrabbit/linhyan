import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print ('begin call')
        return func(*args,**kw)
    print('end call')##此处改动
    return wrapper

@log
def plus(x,y):
    print(x + y)

plus(2,5)