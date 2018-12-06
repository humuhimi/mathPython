class Orange:
    array = []  # 初期化されない クラス変数　データが共有される

    def __init__(self, w, f):
        self.weight = w
        self.fruit = f
        self.array.append((self.weight, self.fruit))
        print('Created')


class Fruits:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # objectナンバーを名前に変更
        return self.name


frt = Fruits("orange")
orl = Orange(10, frt)  # コンポジションフルーツクラスをもつオレンジクラス
orl2 = Orange(15, "dark orange")
orl3 = Orange(20, "white orange")
orlwhite = orl3


print(orl.weight)
print(orl.fruit.name)
print(Orange.array)
# is method は　同一メソッドを返す。
print(orl3 is orlwhite)
print(orl is orl3)



