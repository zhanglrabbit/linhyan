from functools import reduce

def str2num(s):
    try:
        return int(s)
    except Exception as e:
        print(e)
        return float(s)


def calc(exp):
    ss = exp.split('+')         #split是分割函数，这里表示以‘+’为分隔符，将exp分开,返回一个列表
    ns = map(str2num, ss)       #map之前学过，这是将所有的字符串转化为数字
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()