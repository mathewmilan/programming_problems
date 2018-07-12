
#Find Maximum product of 3 nos in a list
def max_product_3(a):
    max_no = None
    max_index = None
    min_no = None
    min_index = None
    max_2prod = None
    max_2index = None
    min_2prod = None
    min_2index = None
    max_3prod = None
    i = 0
    while (i < len(a)):
        if (max_no is None or a[i] > max_no):
            max_no = a[i]
            max_index = i
        if (min_no is None or a[i] < min_no):
            min_no = a[i]
            min_index = i
        i += 1
    i = 0
    while (i < len(a)):
        if (i != max_index):
            if (max_2prod is None or ((a[i] * max_no) > max_2prod)):
                max_2prod = a[i] * max_no
                max_2index = i
        if (i != min_index):
            if (max_2prod is None or ((a[i] * min_no) > max_2prod)):
                max_2prod = a[i] * min_no
                max_2index = i
        i += 1
    i = 0
    while (i < len(a)):
        if (i != min_index):
            if (min_2prod is None or ((a[i] * min_no) < min_2prod)):
                min_2prod = a[i] * min_no
                min_2index = i
        if (i != max_index):
            if (min_2prod is None or ((a[i] * max_no) < min_2prod)):
                min_2prod = a[i] * max_no
                min_2index = i
        i += 1
    i = 0
    while (i < len(a)):
        if ((i != max_index) and ((i != max_2index))):
            if (max_3prod is None or ((a[i] * max_2prod) > max_3prod)):
                max_3prod = a[i] * max_2prod
        if ((i != min_index) and (i != min_2index)):
            if ((max_3prod is None) or (a[i] * min_2prod) > max_3prod):
                max_3prod = a[i] * min_2prod
        i += 1  
    return max_3prod

n_list = [1, 10, -5, 1, -100]
#n_list = [-10, -10, 1, 3, 2]

print(max_product_3(n_list))