from collections import Counter
# 最頻値用のモジュール


def calculate_mean(numbers): # 平均値
    s = sum(numbers)
    N = len(numbers)
    # calculate the mean
    mean = s/N

    return mean
# 中央値(median)を求める


def calculate_median(numbers): # 中央値
    N = len(numbers)
    numbers.sort()

    #  find the  median
    if N % 2 == 0: # 偶数
        m1 = N/2
        m2 = (N/2) + 1
        # 整数変換
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        m = int(m) - 1
        median = numbers[m]

    return median


def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]


def calculate_mode_plus(numbers):
    """
    複数　同数の最頻値がある場合
    :param numbers:
    :return:
    """
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])

    for mode in modes:
        print(mode)
#             ヒットは2妻で?












if __name__ == '__main__':
    donations = [100,60,75,32,130,500,600,600,503,10,230,120,54]
    print(calculate_mean(donations)) # 平均値
    print(calculate_median(donations)) # 中央値
    simplelist = [4,2,1,3,4]
    c = Counter(simplelist)
    # most_commonは出現回数の多い数とその出現回数を返す
    print(c.most_common(1))  # 一番多い奴を出力
    mode = c.most_common(1)
    print(mode[0])  # 出現回数の多い数とその出現回数
    print(mode[0][0])  # 出現回数の多い数だけ

    # scores = [7, 8, 9, 9, 9, 7, 4, 2, 5, 7, 9, 6, 2, 6]
    # mode = calculate_mode(scores)
    # print(mode)
    score = [5,5,5,4,4,4,9,2,7]
    # modes = calculate_mode_plus(score)
    # for mode in modes:
    #     print(mode)
    calculate_mode_plus(score)











