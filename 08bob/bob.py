#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    what = what.strip()
    what = what.replace(",", "")
    what = what.replace(" ", "")

    if what:
        if what.isupper():
            return 'Whoa, chill out!'
        elif what[-1:] == "?":
            return 'Sure.'
        else:
            return 'Whatever.'
    else:
        return 'Fine. Be that way!'

