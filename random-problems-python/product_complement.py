
import pprint

#Find Products Complement in a list
def find_product(num_list):
    products_fwd = []
    products_bwd = []
    products = []
    product = 1
    for no in num_list:
        product *= no 
        products_fwd.append(product)
    pprint.pprint(products_fwd)
    i = 0
    product = 1
    while (i < len(num_list)):
        product *= num_list[-(i+1)]
        products_bwd.insert(-(i+1),product)
        i += 1
    pprint.pprint(products_bwd)
    i = 0
    while (i < len(num_list)):
        if (i == 0):
            products.append(products_bwd[i+1])
        elif(i == len(num_list)-1):
            products.append(products_fwd[i-1])
        else:
            products.append(products_fwd[i-1] * products_bwd[i+1])
        i += 1
    pprint.pprint(products)

a = [1, 7, 3, 4]
#a = [1, 2, 6, 5, 9]
find_product(a)