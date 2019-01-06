"""
draw a square
"""

from matplotlib import pyplot as plt


def draw_square():

    square = plt.Polygon([(1,1),(5,1),(5,5),(1,5)],closed=True)
    # final_ax.add_patch(square)
    # plt.show()
    return square


def draw_circle(x, y):
    circle = plt.Circle((x,y),radius=0.5,fc='w',ec='b')
    return circle


if __name__ == '__main__':
    ax = plt.gca()
    s = draw_square()
    ax.add_patch(s)

    y = 1.5
    while y < 5:
        x = 1.5
        while x < 5:
            c = draw_circle(x,y)
            ax.add_patch(c)
            x += 1.0
        y += 1.0
    plt.axis('scaled')
    plt.show()

    # draw_square()




