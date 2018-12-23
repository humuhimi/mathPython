
from sympy import Symbol,solve,sympify
from sympy.plotting import plot
from sympy.core.sympify import SympifyError


def double_plot_expression(expr1, expr2):
    x = Symbol('x')
    y = Symbol('y')
    expr = solve((expr1, expr2),dict=True)
    solution1 = solve(expr1,y)
    solution2 = solve(expr2,y)
    expression1 = solution1[0]
    expression2 = solution2[0]
    p = plot(expression1,expression2,legend=True,show=False)
    p[0].line_color = 'b'
    p[1].line_color = 'r'
    p.show()
    print("交点の値は" + str(expr[0]))
# 3*x+5*y+2


if __name__ == '__main__':
    expr1 = input('数式1を入力してください')
    expr2 = input('数式2を入力してください')
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('invalid input')
    else:
        double_plot_expression(expr1, expr2)