from sympy import Symbol,solve,sympify
from sympy.plotting import plot
from sympy.core.sympify import SympifyError


def plot_expression(expr):
    y = Symbol('y')
    solution = solve(expr,y)
    expression = solution[0]
    plot(expression)


if __name__ == '__main__':
    expr = input('数式を入力してください')
    try:
        expr = sympify(expr)
    except SympifyError:
        print('invalid input')
    else:
        plot_expression(expr)

