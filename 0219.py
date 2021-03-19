import time

t1 = time.time()
t2 = time.localtime(time.time())
t3 = time.asctime(time.localtime(time.time()))


# print(t3)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print(t3)


f = now
f()
print(f.__name__)