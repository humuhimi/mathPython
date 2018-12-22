"""
print the series of fraction
and calculate it's value
"""

from sympy import Symbol, pprint, init_printing


def print_series(n, x_value):
    # 次数の低い順から並べる
    # init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series,order='rev-lex')
    series_value = series.subs({x:x_value})
    args = "個数:{0},級数:{1},計算結果:{2}"
    print(args.format(n,x_value,series_value))


if __name__ == '__main__':
    n = int(input('個数を入れてください'))
    x = float(input('級数を入力してください'))
    print_series(n,x)





