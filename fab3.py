def fab():
    a = 0
    b = 1
    while True:
        a,b =b, a+b
        yield a

for each in fab():
    if each > 1000:
        break
    print(each,end=" ")
print()
a = [i for i in range(100) if not (i%2) and i%3]     #列表推导式   x%2：不被2整除，   i%3：不被3整除
print(a)
b = {i:i % 2 ==0 for i in range(10) }               #字典推导式   i % 2 ==0  偶数，被2整除
print(b)
c = {i for i in [1,2,3,4,4,5,23,43,234,13,1,2,2,2]}     #集合推导式
print(c)
d =  "i for in 'i love fishc.com'"
print(d)
e =(i for i in range(10))           #generator
print(e)