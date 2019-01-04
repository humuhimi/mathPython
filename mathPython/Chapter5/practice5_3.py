import random


def money_game(money):

    stock = money
    coin = {'表': 1, '裏': 0}
    coin_list = list(coin.keys())
    toss = random.randint(0,1)
    win_ammount = 1
    loss_ammount = 1.5

    while stock > 0:

        if coin['表'] == toss:
            stock += win_ammount
            result = coin_list[0]
        else: # 裏なら
            stock -= loss_ammount
            result = coin_list[1]

        print('{0}です!残金:{1}'.format(result, stock))
    print('ゲームは終了しました')


if __name__ == '__main__':

    money = float(input('enter your first amount'))
    money_game(money)



