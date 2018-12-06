"""
fractions operations
"""
from fractions import Fraction


def add(a,b):
    print('足し算結果: {0}'.format(a+b))


def sub(a,b):
    print('引き算結果: {0}'.format(a-b))


def multi(a,b):
    print('掛け算結果: {0}'.format(a * b))


def divi(a,b):
    print('割り算結果: {0}'.format(a / b))


if __name__ == '__main__':
    try:
        a = Fraction(input('最初の数字'))
        b = Fraction(input('次のの数字'))
        op = input('操作-足し算、引き算、掛け算、割り算')
        if op == '足し算':
            add(a,b)
        if op == '引き算':
            sub(a,b)
        if op == '掛け算':
            multi(a,b)
        if op == '割り算':
            divi(a,b)

    except Exception:
        pass


