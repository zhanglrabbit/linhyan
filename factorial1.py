def factorial(n):
    if n == 1:
        return  1
    else:
        return n * factorial(n-1)

#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

num = int(input('请输入一个正整数：'))
result = factorial(num)
print("%d 的阶乘是：%d" % (num, result))