import matplotlib.pyplot as plt
import random


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
    transformations = [transform_1, transform_2, transform_3]
    # p[0] = 0
    # p[1] = 0
    x = [0]
    y = [0]

    x1, y1 = 0,0

    while n > 0:
        rand_index = random.randint(0, 2)
        t = transformations[rand_index]
        p = (x1, y1)
        x1, y1 = t(p)
        x.append(x1)
        y.append(y1)
        n -= 1

    return x, y


if __name__ == '__main__':

    n = int(input('試行回数を入力してください'))
    x, y = sierpinski_gasket(n)
    # ax = plt.axis(xmin=0,ymin=0)
    plt.plot(x,y,'o')
    plt.title('sierpinski with {0} point'.format(n))
    plt.show()

