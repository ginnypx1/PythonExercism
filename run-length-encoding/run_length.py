def decode(codestring):
    # 12WB12W3B24WB to WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB
    decode_string = ""
    # while the string exists
        # if next is a number
            # 1. detach number, store as count
            # 2. detach next letter, multiply by count
            # 3. append to codestring
        # if next is a letter
            # append single letter to codestring
    return codestring

def encode(codestring):
    # WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB to 12WB12W3B24WB
    encode_string = ""
    count = 1
    i = 1
    # while the string exists
    while i < len(codestring):
        # if current letter matches next letter
        if codestring[i-1] == codestring[i]:
            # count += 1
            count += 1
            i += 1
            last_letter = codestring[i-1]
        else:
            # append encode_string count + repeated letter
            if count == 1:
                encode_string =  encode_string + codestring[i-1]
            else:
                encode_string =  encode_string + str(count) + codestring[i-1]
            # reset count to 1
            count = 1
            i += 1
    if count == 1:
        encode_string =  encode_string + codestring[i-1]
    else:
        encode_string =  encode_string + str(count) + codestring[i-1]     
    return encode_string
