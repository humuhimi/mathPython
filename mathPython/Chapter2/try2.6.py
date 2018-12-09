"""
Example of drawing a horizontal bar chart
"""

import matplotlib.pyplot as plt


def create_bar_chart(data,labels):

    """ nuber of bar"""
    num_bars = len(data)
    # this list is the point on the y-axis where each
    positions = range(1,num_bars+1)
    plt.barh(positions,data,align='center')
    # set the label of each bar
    plt.yticks(positions,labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title('Number of steps walked')
    # turn the grid which may assist in virtual estimation
    plt.grid()
    plt.show()


if __name__ == '__main__':
    steps = [6534,7000,8900,10786,3467,11045,5095]
    labels = ['Sun','Mon','Tue','Wed','thu','Fri','Sat']
    create_bar_chart(steps,labels)






