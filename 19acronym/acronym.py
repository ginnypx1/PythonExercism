def abbreviate(phrase):
    '''Converts a long name into its acronym'''
    abbreviation = []

    phrase = phrase.replace("-", " ")
    phrase_words = phrase.split(" ")
    
    for word in phrase_words:
        first_letter = word[:1].upper()
        abbreviation.append(first_letter)
        
        # handle camelCase
        if word[1:2].islower():
            for letter in word[1:]:
                if letter.isupper():
                    abbreviation.append(letter)

    return "".join(abbreviation)
