"""
二次関数電卓
"""
import matplotlib.pyplot as plt

# x_values = [-1,0,1,2,3,4,5,6,7,8,9,10,11]
x_values = range(-100,100,1)
y_values = []
for x in x_values:  # 二次関数計算
    y = x**2 +x*2 + 1
    y_values.append(y)
    print('x={0},y={1}'.format(x, y))
plt.plot(x_values,y_values)
plt.show()





