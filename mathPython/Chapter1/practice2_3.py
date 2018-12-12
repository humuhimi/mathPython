"""
show Expenditure
"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager

categories_num = input('カテゴリー数を入れてください')
category = []  # カテゴリーはいる
expenditure = []  # 費用

while True:
    category.append(input('カテゴリーは何ですか?'))
    expenditure.append(input('費用を入力ください'))
    if len(expenditure) == int(categories_num):  # pythonでは==は型も同じじゃないとあかんのか
        break

plt.rcParams['font.family'] = 'AppleGothic'
plt.ylim(0,60000)
plt.title('支出')
plt.xlabel('カテゴリ')
plt.ylabel('費用')
plt.bar(category, expenditure, align='center')
plt.show()







