import random


def money_game(money):

    stock = int(money)
    coin = {'表': 1, '裏': 0}
    coin_list = list(coin.keys())

    while stock > 0:

        if coin['表'] == random.randint(0,1):
            stock += 1
            result = coin_list[0]
        else: # 裏なら
            stock -= 1.5
            result = coin_list[1]

        print('{0}です!残金:{1}'.format(result, stock))
    print('ゲームは終了しました')


if __name__ == '__main__':

    money = input('enter your first amount')
    money_game(money)



