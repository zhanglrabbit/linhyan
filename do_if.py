# -*- coding: utf-8 -*-
# height.replace('.','').isdigit()用于判断输入是否为小数，如去掉replace函数，则不能判断带有小数点的字符

def main():
    height = get_height()
    weight = get_weight()
    result = bmi(height, weight)
    print('当前输入身高为：{0}米，体重为{1}千克，BMI值为{2}，体形{3}'.format(
        height, weight, result[0], result[1]))


def get_height():
    while True:
        height = input('请输入身高(单位：米)，范围为0.5m-3m\n')
        if height.replace('.', '').isdigit() is True:
            float_height = float(height)
            if 0.5 <= float_height <= 3:
                return float_height
            else:
                print('必须输入介于0.5到3之间的数字')
                continue
        else:
            print('输入其它字符了，必须输入介于0.5到3之间的数字')
            continue


def get_weight():
    while True:
        weight = input('请输入体重(单位：千克)，范围为2KG-200KG\n')
        if weight.replace('.', '').isdigit() is True:  # 若不用replace方法将小数点替换，则无法判断输入是否小数
            float_weight = float(weight)
            if 2 <= float_weight <= 200:
                return float_weight
            else:
                print('必须输入介于2到200之间的数字')
                continue
        else:
            print('输入其它字符了，必须输入介于2到200之间的数字')
            continue


def bmi(height, weight):
    li = []
    bmi = round(weight/height**2, 2)
    li.append(bmi)
    if bmi < 18.5:
        li.append('过轻')
    elif 18.5 <= bmi < 25:
        li.append('正常')
    elif 25 <= bmi < 28:
        li.append('肥胖')
    else:
        li.append('非常肥胖')
    return list(li)

if __name__ == '__main__':
    main()

print(__name__)
#print(__dir__)
#print(__all__)
#print(__class__)
print(__file__)
print(__doc__)
