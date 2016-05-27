def slices(numstring, slice_value):
    """Chops a given string of numbers into all possible consecuctive slices of the given length"""
    if (slice_value == 0) or (slice_value > len(numstring)):
        raise ValueError("Length argument doesn't fit the series.")

    slice_list = []
    # convert string to list of numbers
    intlist = [int(num) for num in numstring]
    # find subsets
    for i in range(0, (len(numstring)-slice_value+1)):
        slice_list.append(intlist[i: i+slice_value])
    return slice_list

if __name__ == '__main__':
    print(slices("97867564", 2)) 
    print(slices("97867564", 3)) 