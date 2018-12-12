"""
create line graph and bar chart of today temperature
"""
import matplotlib.pyplot as plt
from matplotlib import matplotlib_fname,get_cachedir
from matplotlib.font_manager import FontProperties,fontManager
# fp = FontProperties(fname='/Users/humu/matplotlib/ipaexg00301/ipaexg.ttf ')


Y = [5.0,5.0,6.0,8.0,11.0,12.0,10.0,9.0]  # 気温
# y = [5,5,6,8,11,12,10,9]  # 気温
# x = [2, 5, 8, 11, 14, 17, 20, 23]  # 対応時間
X = [2.0, 5.0, 8.0, 11.0, 14.0, 17.0, 20.0, 23.0]  # 対応時間
# fp = FontProperties(Users/humu/ipaexg00301)


class GraphMaker:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        plt.rcParams['font.family'] = 'AppleGothic'
        plt.title('今日のおん度をグラフで出してみた')  # 後日調べる
        plt.xlabel('時間')  # 流用したい
        plt.ylabel('今日のおん度')  # 流用したい
        plt.xticks(self.x)
        # plt.yticks(self.y)

    @staticmethod
    def plot_maintain():
        """"
        maintain or fix for plot
        """
        print(matplotlib_fname())
        print(get_cachedir())
        print([f.name for f in fontManager.ttflist])

    def create_graph(self):
        plt.plot(self.x, self.y, marker='o')  # 流用したい
        plt.show()

    def create_bar_chart(self):
        plt.bar(self.x,self.y,align='center')
        plt.show()


graph = GraphMaker(X,Y)
graph.create_graph()
graph.create_bar_chart()









