#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    what = what.strip()
    what = what.replace(",", "")
    what = what.replace(" ", "")
    if what:
        if what[-1:] == "?":
            what = what.replace("?", "")
            if what.isdigit():
                return 'Sure.'
            elif what == what.upper():
                return 'Whoa, chill out!'
            else:
                return 'Sure.'
        elif what == what.upper():
            if what.isdigit():
                return 'Whatever.'
            else:
                return 'Whoa, chill out!'
        else:
            return 'Whatever.'
    else:
        return "Fine. Be that way!"
