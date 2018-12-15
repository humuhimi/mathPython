def find_corr_x_y(x,y):
    n = len(x)
    #  find sum of product
    prod = []
    for xi, yi in zip(x,y):
        prod.append(xi*yi)
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)


