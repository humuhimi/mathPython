def find_corr_x_y(x,y):
    # if len(x) != len(y):
    n = len(x)
    try:
        n2 = len(y)
        if n != n2:
            raise ValueError("invalid length of args!!")
    except(Exception,ValueError) as e:
        print(e)
    else:
        #  find sum of product
        prod = []
        for xi, yi in zip(x,y):
            prod.append(xi*yi)
        sum_prod_x_y = sum(prod)
        sum_x = sum(x)
        sum_y = sum(y)
        squared_sum_x = sum_x**2
        squared_sum_y = sum_y**2
        x_square = []
        for xi in x:
            x_square.append(xi**2)
        # find the sum
        x_square_sum = sum(x_square)
        y_square = []
        for yi in y:
            y_square.append(yi**2)
        y_square_sum = sum(y_square)

        # use formula to calculate correlation
        numerator = n*sum_prod_x_y - sum_x*sum_y
        denominator_item1 = n*x_square_sum - squared_sum_x
        denominator_item2 = n*y_square_sum - squared_sum_y
        denominator = (denominator_item1*denominator_item2)**0.5
        correlation = numerator/denominator

        return correlation


x = [1,2,3]
y = [4,6]

print(find_corr_x_y(x,y))


