from sympy import Symbol, summation, pprint


def calc_sum_result(express,num):
    n = Symbol('n')
    s = summation(express, (n, 1, num))
    return s


if __name__ == '__main__':
    pref = input('式を入力してください')
    nums = input('nに入れる回数を入力してください')
    answer = calc_sum_result(pref, nums)
    pprint(answer)
