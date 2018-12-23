from sympy import Symbol,factor,simplify,pprint,solve
from sympy.core.sympify import SympifyError


def find_factor(pref):
    x = Symbol('x')
    y = Symbol('y')

    factor_pref = factor(pref)
    solve_pref = solve(pref, x, dict=True)
    pprint(factor_pref)
    print(solve_pref)


if __name__ == '__main__':

    pref = input('式を入力してください')
    try:
        pref = simplify(pref)
    except SympifyError:
        print('Invalid input pref')
    else:
        find_factor(pref)