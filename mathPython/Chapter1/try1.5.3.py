'''
Unit Convert:Miles and Kilometers
'''


def print_menu():
    print('1. kilometers to Miles')
    print('2. Miles to Kilometers')


def km_miles():
    km = float(input('km距離入れろ:'))
    miles = km / 1.609
    print('Distance in miles:{0}'.format(miles))


def miles_km():
    miles = float(input('mile距離入れろ:'))
    km = miles * 1.609
    print('Distance in km:{0}'.format(km))


if __name__ == '__main__':
    print_menu()

    choice = input('どちらのメニュ:?')

    if choice == '1':
        km_miles()

    if choice == '2':
        miles_km()





