"""
Frequency table for list of numbers
"""

from collections import Counter


def frequency_table(numbers):
    table = Counter(numbers)
    number_freq = table.most_common()
    number_freq.sort()
    print('Number\nFrequency')
    for number in number_freq:
        print('{0}\t{1}'.format(number[0],number[1]))


if __name__ == '__main__':
    scores = [7,8,9,5,2,6,3,7,8,5,2,1]
    frequency_table(scores)

