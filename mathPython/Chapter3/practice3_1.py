def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    # calculate the mean
    mean = s/N

    return mean
# 中央値(median)を求める


def calculate_median(numbers):
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


if __name__ == '__main__':
    donations = [100,60,75,32,130,500,600,600,503,10,230,120,54]
    print(calculate_mean(donations)) # 平均値
    print(calculate_median(donations)) # 中央値





