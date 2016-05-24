#
# Skeleton file for the Python "Bob" exercise.
#
def hey(what):
    what = what.strip()

    if what.isupper():
        return 'Whoa, chill out!'
    elif what[-1:] == "?":
        return 'Sure.'
    elif what:
        return 'Whatever.'
    else:
        return 'Fine. Be that way!'