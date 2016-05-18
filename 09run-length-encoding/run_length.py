def decode(codestring):
    # 12WB12W3B24WB to WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB
    decode_string = ""
    count = 1
    i = 1

    while i <= len(codestring):
        # pop first item off
        item = codestring[i-1]
        # if it's a number, store
        if item.isdigit():
            count = int(item)
            # if next number is also a number, pop off and store
            if codestring[i].isdigit():
                next_num = codestring[i]
                count = int(str(count) + next_num)
                i += 1
            i += 1
        else:
            # decode_string adds that letter times count
            decode_string = decode_string + (item * count)
            i +=1
            count = 1
    decode_string = decode_string + (item * (count-1))
    return decode_string



def encode(codestring):
    # WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB to 12WB12W3B24WB
    encode_string = ""
    count = 1
    i = 1

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



if __name__ == '__main__':
    print(decode('12WB12W3B24WB'))