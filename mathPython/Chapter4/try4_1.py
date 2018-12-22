"""
print the series of fraction
and calculate it's value
"""

from sympy import Symbol, pprint, init_printing


def print_series(n):
    # 次数の低い順から並べる
    # init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series,order='rev-lex')


if __name__ == '__main__':
    n = int(input('数字を入れてください'))
    print_series(n)





