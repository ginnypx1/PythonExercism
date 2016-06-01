from functools import reduce


def sum_of_multiples(limit, num_array):
    '''When given a number, finds the sum of all the multiples of particular numbers up to but not including that number.'''
    
    multiples = []
    
    # find multiples for each value in the array
    for num in num_array:
        if num == 0:
            pass
        else:
            multiples += list(filter(lambda x: x%num == 0, range(1,limit)))

    # filter out repeated values
    multiples = list(set(multiples))

    # reduce multiples to a single sum value
    if multiples:
        single_sum = reduce(lambda x, y: x+y, multiples)
    else:
        single_sum = 0

    return single_sum