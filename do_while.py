#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 计算1+2+3+...+100:
sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)

# 计算1x2x3x...x100:
acc = 1
n = 1
while n <= 10:
    acc = acc * n
    n = n + 1
print(acc)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n, end=" ")

print()

n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n, end=" ")
    n = n + 1

# print('END')
