

def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest - lowest
    return lowest,highest,r


if __name__ == '__main__':
    donations = [100,300,400,500]
    lowest,highest,r = find_range(donations)
    print('lowest:{0}\thighest:{1}\tRange:{2}'.format(lowest,highest,r))




