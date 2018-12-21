# USAデータから年ごとのデータ取得し配列に格納
# 平均値,中央値、分散、標準偏差を計算
# プロットして計算
# 使うデータ:'USA_SP_POP_TOTL.csv'

from Chapter3.practice3_1 import calculate_mean,calculate_median,calculate_mode,calculate_mode_plus
from Chapter3.practice3_2 import frequency_table
from Chapter3.practice3_4 import find_differences,calculate_variance
import csv
import matplotlib.pyplot as plt


def csv_plot(x,y):
    plt.plot(x,y)
    plt.xlabel('years')
    plt.ylabel('population')
    plt.show()


def get_csv(filename):
    global years
    global population
    #  shadowing names はlocal変数を外で使うときに生じるので、globalをつけて具体化する
    years = []  # x
    population = []  # y

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for data in reader:
            years.append(data[0])
            population.append(float(data[1]))
    years.reverse()
    population.reverse()
    return years,population


if __name__ == '__main__':

    years,population = get_csv('USA_SP_POP_TOTL.csv')
    csv_plot(years,population)
    print(calculate_mean(population))
    print(calculate_median(population))
    print(calculate_variance(population))
    print(calculate_mode_plus(population))












