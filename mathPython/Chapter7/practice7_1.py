"""
・微分可能であること

1.関数と変数の値を受ける
2.入力された値が連続かどうかをチェックする。
"""
from sympy import Symbol,Derivative,sympify
import math


def check_continuity(func,var,continuity):
    var = Symbol('var')
    function = func
    d = Derivative(function,var)
    if d == continuity:
        return True
    else:
        return False


if __name__ == '__main__':
    func = input('関数を入力してください')
    var = input('変数をいれてください')
    continuity = int(input('連続する点の数を入力してください'))

    if check_continuity(func,var,continuity):

        print('{0}is continuous at {1}'.format(func,continuity))
    else:
        print('{0}is not continuous at {1}'.format(func, continuity))


