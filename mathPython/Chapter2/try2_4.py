"""
the relaitonship between graviational force and
distance between two bodies
"""

import matplotlib.pyplot as plt
# draw the graph


def draw_graph(x,y):
    plt.plot(x,y,marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitional force in newtons')
    plt.title('Gravitional force and distance')
    plt.show()


def generate_f_r():
    """
    generate values for r
    :return:
    """


r = range(100,1001,50)
# empty list to store the calculated values of F
F = []
# constant,G
G = 6.674*(10**-11)
# two masses
m1 = 0.5
m2 = 1.5
# calculate Force and add it to list,F
for dist in r:
    force = G*(m1*m2)/(dist**2)
    F.append(force)
# call the draw_graph function
draw_graph(r,F)
#
# if __name__ == '__main__':
#     generate_f_r(r,F)





