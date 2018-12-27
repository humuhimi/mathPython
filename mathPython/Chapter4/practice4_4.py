from sympy import Symbol, Poly,pprint, solve_poly_inequality,solve_rational_inequalities,solve_univariate_inequality,sympify,sin
from sympy.core.sympify import SympifyError


def isolve(expr):
    if expr.is_polynomial():
        pprint(solve_poly(expr))
    elif expr.is_rational_function():
        pprint(solve_rational(expr))
    else:
        pprint(solve_univariate(expr))


def solve_poly(expr):

    x = Symbol('x')
    ineq_obj = expr
    lhs = ineq_obj.lhs
    p = Poly(lhs,x)
    rel = ineq_obj.rel_op
    return solve_poly_inequality(p, rel)


def solve_rational(expr):

    x = Symbol('x')
    ineq_obj = expr
    lhs = ineq_obj.lhs
    numer,denom = lhs.as_numer_denom()
    p1 = Poly(numer)
    p2 = Poly(denom)
    rel = ineq_obj.rel_op
    return solve_rational_inequalities([[((p1, p2), rel)]])


def solve_univariate(expr):

    x = Symbol('x')
    ineq_obj = expr
    return solve_univariate_inequality(ineq_obj, x, relational=False)


if __name__ == '__main__':
    expr = input('式を入力してください')

    try:
        expr = sympify(expr)

    except SympifyError:
        print('invalid input expression')

    else:
        isolve(expr)


