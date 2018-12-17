import csv
import matplotlib.pyplot as plt

from Chapter3.practice3_5 import find_corr_x_y


def scatter_plot(x,y):
    plt.scatter(x,y)
    plt.xlabel('summer')
    plt.ylabel('swimming-school_correlation')
    plt.show()


def read_csv(filename):

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        summer = []
        highest_correlated = []

        for row in reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))
            if len(summer) == 100:
                break
    return summer,highest_correlated


if __name__ == '__main__':
    summer, highest_correlated = read_csv('correlate-summer.csv')
    corr = find_corr_x_y(summer,highest_correlated)
    print('Highest correlation:{0}'.format(corr))
    scatter_plot(summer,highest_correlated)
#     関数先書いてからimportを自動選択した方がいい
