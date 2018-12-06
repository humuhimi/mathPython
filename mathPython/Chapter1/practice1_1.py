"""
奇数偶数判定
"""


def odd_even_decision(a):

    list_even = []
    list_odd = []
    List = (list_even,list_odd)

    if a % 2 == 0:
        print("偶数です")
        for i in range(10):
            i *= 2
            list_even.append(a + i)
    else:
        print("奇数です")
        for j in range(10):
            if j % 2 != 0:
                continue
            list_odd.append(a + j)

    # for List in range(10):
    #     print(List)
    print(List)


if __name__ == '__main__':

    a = int(input("数字を入力してください"))
    odd_even_decision(a)






