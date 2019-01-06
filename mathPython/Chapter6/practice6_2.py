import matplotlib.pyplot as plt
import math
import random
"""

変換の確率はどれも同じ=1/3
シェルピンスキー関数で1/3の確率で変換のどれかを読み出す。
その値を記録する。
開始は(0,0)から2点をまとめるp[0,1]
pは変化する点
x,yは点の記録
"""


def transform_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5*x
    y1 = 0.5*y

    return x1,y1


def transform_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5

    return x1, y1


def transform_3(p):
    x = p[0]
    y = p[1]

    x1 = 0.5 * x + 1.0
    y1 = 0.5 * y

    return x1, y1


def sierpinski_gasket(n):

    p[0] = 0
    p[1] = 0
    x = [0]
    y = [0]

    transformations = [transform_1,transform_2,transform_3]
    x1, y1 = 0,0
    rand_index = random.randint(0,2)

    while n > 0:
        t = transformations[rand_index]
        p = t(p)
        x.append(p[0])
        y.append(p[1])
        n -= 1

    return x,y


if __name__ == '__main__':

    n = int(input('試行回数を入力してください'))
    x, y = sierpinski_gasket(n)
    ax = plt.axis(xmin=0,ymin=0)
    plt.plot(x,y,'o')
    plt.title('sierpinski with {0}point'.format(n))
    plt.show()

