# 输入汉诺伊塔的层数 输出移动步骤 和总步骤数

temp = int(input('输入汉诺伊塔的层数：'))


def hanoi(temp, x, y, z):
    step = 0
    if temp == 1:
        print(x, '→', z)  # 把x上的方块移动到z上
        step += 1

    else:
        hanoi(temp - 1, x, z, y)  # 把x上temp-1个方块放到y上
        step += 1
        print(x, '→', z)  # 把x上的方块移动到z上
        step += 1
        hanoi(temp - 1, y, x, z)  # 把y上的temp-1个方块放到z上
        step += 1  # 每次移动 步数都自增1

    print('你移动了', step, '步')


hanoi(temp, 'X', 'Y', 'Z')
