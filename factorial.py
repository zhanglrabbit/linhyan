def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


num = int(input('请输入一个正整数：'))
result = factorial(num)
print("%d 的阶乘是：%d" % (num, result))
#help(print)
#print(print.__doc__)
