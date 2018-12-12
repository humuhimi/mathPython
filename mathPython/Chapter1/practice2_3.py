"""
show Expenditure
"""
categories_num = input('カテゴリー数を入れてください')
category = []
expenditure = []

while True:
    category.append(input('カテゴリーは何ですか?'))
    expenditure.append(input('費用を入力ください'))
    if len(expenditure) == int(categories_num): # pythonでは==は型も同じじゃないとあかんのか
        print('breakできるはず')
        break





