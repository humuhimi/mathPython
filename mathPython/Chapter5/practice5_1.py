"""
Draw venn diagram for two sets
"""

from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet
import csv


def draw_venn(sets):
    venn2(subsets=sets,set_labels=('Football','Others'))
    plt.show()


def read_csv(filename):
    football = []
    others = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == '1':
                football.append(row[0])
            if row[2] == '1':
                others.append(row[0])
    return football, others


if __name__ == '__main__':
    s1 = FiniteSet(1,3,5,7,9,11,13,15,17,19)
    s2 = FiniteSet(2,3,4,5,7,11,13,17,19)
    draw_venn([s1,s2])
    # football, others = read_csv('sports.csv')
    # draw_venn(football, others)


