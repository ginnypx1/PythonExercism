def encode(codestring):
    '''alphabet to reverse alphabet in groups of 5 letters'''
    
    # format the codestring
    codestring = codestring.lower()
    codestring = codestring.replace(" ", "")
    codestring = codestring.replace(",", "")
    codestring = codestring.replace(".", "")

    # encode into reverse alphabet, no groups of 5 letters
    encode_string = codestring.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))

    if len(encode_string) < 5:
        return encode_string
    else:
        # create the groups of five letters
        i = 0
        encode_list = []
        while i <= len(encode_string):
            encode_list.append(encode_string[i:i+5])
            encode_list.append(" ")
            i += 5
        return "".join(encode_list).strip()
        

def decode(codestring):
    '''reverse alphabet to alphabet, combining into one string'''
    codestring = codestring.replace(" ", "")
    decode_string = codestring.translate(str.maketrans('zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz'))
    return decode_string