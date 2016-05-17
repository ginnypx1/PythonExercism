#pangram - a sentence that contains all the letters of the alphabet

def is_pangram(pangramString):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(pangramString.lower())
