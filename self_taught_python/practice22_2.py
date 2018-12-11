
def bottles_of_beer(bob):
    """
    Prints Bottle of Beer on the Wall lyrics.
    :param bob: Must be a positive integer
    :return:
    """
    if bob < 1:
        print("""no more beer """)
        return

    tmp = bob
    bob -= 1
    print("""{}bottle of beer on the wall.
    {}bottle of beer.
    Take one down,
    {} bottles of beer on the wall""".format(tmp,tmp,bob))
    bottles_of_beer(bob)


if __name__ == '__main__':
    bottles_of_beer(99)
