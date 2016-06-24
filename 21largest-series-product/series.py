from functools import reduce
from operator import mul

def slices(numstring, slice_length):
    """Chops a given string of numbers into all possible consecuctive slices of the given length
        var numstring: a string of numbers
        var slice_length: int of the length of the slice desired
        Returns a value error if the slice_length is zero or longer than the numstring
    """
    if (slice_length == 0) or (slice_length > len(numstring)):
        raise ValueError("Length argument doesn't fit the series.")

    return [list(map(int, numstring[i:i+slice_length])) 
            for i in range(len(numstring)-slice_length+1)]


def largest_product(numstring, slice_length):
    """Returns the value of the largest product created in the various slices of numstring
        var numstring: a string of numbers
        var slice_length: int of the length of the slice desired
        Returns a value error if the slice_length is zero or longer than the numstring
    """
    if slice_length == 0:
        return 1
    elif (slice_length > len(numstring)) or (slice_length < 0):
        raise ValueError("Length argument doesn't fit the series.")
    else:
        all_products = []
        # find all of the products
        for every_slice in slices(numstring, slice_length):
            slice_product = reduce(mul, every_slice)
            all_products.append(slice_product)
        return max(all_products)
