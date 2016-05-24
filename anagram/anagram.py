def detect_anagrams(word, wordlist):
    anagram_list = []
    word = word.lower()
    # create a master list
    sort_word = sorted(word)
    # find matches
    for each_word in wordlist:
        if sort_word == sorted(each_word.lower()):
            if each_word.lower() != word:
                anagram_list.append(each_word)
    return anagram_list