def slices(numstring, slice_value):
    """Chops a given string of numbers into all possible consecuctive slices of the given length"""
    i = 0
    slice_list = []
    while slice_value <= len(numstring):
        # grab a string slice and turn it into an array of ints
        intlist = list(map(lambda x: int(x), numstring[i:slice_value]))
        # if it's not empty, append it to results lists
        if intlist:
            slice_list.append(intlist)
        # increase the variables
        i += 1
        slice_value += 1
    # if there is a results list, return it, or raise a value error
    if slice_list:
        return slice_list
    else:
        raise ValueError("Length argument doesn't fit the series.")