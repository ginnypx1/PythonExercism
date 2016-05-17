from collections import Counter
import re

def word_count(text):
    """Counts how many times a word is in a block of text"""
    text = text.lower()
    text = text.replace("_", " ")
    words = re.findall("[\w']+", text)
    return dict(Counter(words))
