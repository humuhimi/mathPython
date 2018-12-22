from sympy import expand, sympify
from sympy.core.sympify import SympifyError


def product(expr1, expr2):

    prod = expand(expr1 * expr2)
    print(prod)


if __name__ == '__main__':
    expr1 = input('数式1を入れてください')
    expr2 = input('数式2を入れてください')
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('invalid input error')
    else:
        product(expr1,expr2)

