def word_count(text):
    """ Tells how many times a word is in a block of text"""
    text = text.lower()
    text = text.replace()
    text_list = text.split(" ")
    word_dict = {}
    for word in text_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict
