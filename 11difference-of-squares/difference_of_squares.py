from functools import reduce

def square_of_sum(num):
    '''Sum the numbers, then square the total'''
    # create range
    num_list = list(range(1, num+1))
    # reduce range
    reduced_num = reduce(lambda x,y: x+y, num_list)
    # square the total
    square_of_sum = reduced_num**2
    return square_of_sum


def sum_of_squares(num):
    '''Square each number, then add all those together'''
    # create range
    num_list = list(range(1, num+1))
    # map over range, square each
    map_list = list(map(lambda x: x**2, num_list))
    # reduce range
    sum_of_squares = reduce(lambda x,y: x+y, map_list)
    return sum_of_squares


def difference(num):
    '''Returns the difference between the square of sums and the sum of squares'''
    return square_of_sum(num) - sum_of_squares(num)