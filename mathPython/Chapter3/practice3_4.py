def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    # calculate
    mean = s/N
    return mean


def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []

    for num in numbers:
        diff.append(num - mean)
    return diff


def calculate_variance(numbers):

    diff = find_differences(numbers)
    #  find the squared difference
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance


if __name__ == '__main__':
    donations = [100,60,50,30,50,70,90,40,80]
    variance = calculate_variance(donations)
    print('分散:{}'.format(variance))
    std = variance**0.5
    print('標準偏差:{}'.format(std))





