'''
Multiplication table printer
'''


def multi_table(a):
    for i in range(1,11):
        print('{0} x {1} = {2}'.format(a, i, a*i))
#         float指定しないと、文字列として認識される


if __name__ == '__main__':
    a = input('Enter a number:')
    multi_table(float(a))


