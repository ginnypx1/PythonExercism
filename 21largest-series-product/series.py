from functools import reduce

def slices(numstring, slice_value):
    # from Python program #14
    """Chops a given string of numbers into all possible consecuctive slices of the given length"""
    slice_list = []
    # convert string to list of numbers
    intlist = [int(num) for num in numstring]
    # find subsets
    for i in range(0, (len(numstring)-slice_value+1)):
        slice_list.append(intlist[i: i+slice_value])
    return slice_list

def largest_product(numstring, slice_value):
    if slice_value == 0:
        return 1
    elif (slice_value > len(numstring)) or (slice_value < 0):
        raise ValueError("Length argument doesn't fit the series.")
    else:
        all_products = []
        largest = 0
        # split into the relevant slices
        slice_list = slices(numstring, slice_value)
        # find all of the products
        for every_slice in slice_list:
            slice_product = reduce(lambda x,y: x*y, every_slice)
            all_products.append(slice_product)
        # find the largest product
        for product in all_products:
            if product > largest:
                largest = product
        return largest