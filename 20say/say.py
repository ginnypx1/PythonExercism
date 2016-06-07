FIRST_TEN = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine']
SECOND_TEN = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
              'sixteen', 'seventeen', 'eighteen', 'nineteen']
OTHER_TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
              'eighty', 'ninety']


def singleDigit(number):
    '''handles the numbers zero through 9'''
    return FIRST_TEN[number]

def doubleDigit(n):
    '''handles the numbers 10-99'''
    # to handle the teens
    if n[0] == '1':
        return SECOND_TEN[int(n) - 10]
    # to handle the "tys"
    elif n[1] == '0':
        return OTHER_TENS[int(n[0]) - 2]
    # all other two-digit numbers
    else:
        return OTHER_TENS[int(n[0]) - 2] + '-' + singleDigit(int(n[1]))

def hundreds(n):
    '''handles the numbers 100-999'''
    what_hundred = singleDigit(int(n[0])) + ' hundred'
    # if no value
    if n == '000':
        return ''
    # if single digit value
    elif n[0] == '0' and n[1] == '0':
        return singleDigit(int(n[2]))
    # if double digit value
    elif n[0] == '0':
        return doubleDigit(n[1:3])
    # ending in double zero (100, 200, 300, 400, 500, 600, 700, 800, 900)
    elif n[1] == '0' and n[2] == '0':    
        return what_hundred
    # 101, 102, 202, etc.
    elif n[1] == '0':
        return what_hundred + ' and ' + singleDigit(int(n[2]))
    else:
        return what_hundred + ' and ' + doubleDigit(n[1:3])

def thousands(n):
    '''handles the numbers 1000-9999'''
    what_hundreds = hundreds(n[1:4])
    if what_hundreds:
        if what_hundreds[0] == '0':
            return singleDigit(int(n[0])) + ' thousand and ' + what_hundreds
        else:
            return singleDigit(int(n[0])) + ' thousand ' + what_hundreds 
    else:
        return singleDigit(int(n[0])) + ' thousand'

def ten_thousands(n):
    '''handles the numbers 10000-99999'''
    return doubleDigit(n[0:2]) + ' thousand ' + hundreds(n[2:5])

def hundred_thousands(n):
    '''handles the numbers 100000-999999'''
    what_hundred_thousands = hundreds(n[0:3]) 
    what_hundreds = hundreds(n[3:6])
    if what_hundred_thousands:
        return what_hundred_thousands + ' thousand ' + what_hundreds
    else:
        if n[3] == '0' and n[5] == '0':
            return what_hundreds
        else:
            return 'and ' + what_hundreds

def millions(n):
    '''handles 1000000 to 9999999'''
    if n[1:7] == '000000':
        return singleDigit(int(n[0])) + ' million'
    else:
        return singleDigit(int(n[0])) + ' million ' + hundred_thousands(n[1:7])

def ten_millions(n):
    '''handles the numbers 10000000-99999999'''
    return doubleDigit(n[0:2]) + ' million ' + hundred_thousands(n[2:8])

def hundred_millions(n):
    '''handles the numbers 100000000-999999999'''
    return hundreds(n[0:3]) + ' million ' + hundred_thousands(n[3:9])

def billions(n):
    '''handles 1000000000 to 9999999999'''
    if n[1:10] == '000000000':
        return singleDigit(int(n[0])) + ' billion'
    else:
        return singleDigit(int(n[0])) + ' billion ' + hundred_millions(n[1:10])

def ten_billions(n):
    '''handles 10000000000 to 99999999999'''
    return doubleDigit(n[0:2]) + ' billion ' + hundred_millions(n[2:11])

def hundred_billions(n):
    '''handles 100000000000 to 999999999999'''
    return hundreds(n[0:3]) + ' billion ' + hundred_millions(n[3:12])


def say(number):
    '''Turns a number 0 - 999,999,999,999 into speech text'''
    n = str(number)
    if n[0] == '-':
        raise AttributeError("please enter a positive number")

    number = int(number)
    n = str(number)
    result = ""

    if len(n) == 1:
        result = singleDigit(number)

    elif len(n) == 2:
        result = doubleDigit(n)

    elif len(n) == 3:
        result = hundreds(n)

    elif len(n) == 4:
        result = thousands(n)

    elif len(n) == 5:
        result = ten_thousands(n)

    elif len(n) == 6:
        result = hundred_thousands(n)

    elif len(n) == 7:
        result = millions(n)

    elif len(n) == 8:
        result = ten_millions(n)

    elif len(n) == 9:
        result = hundred_millions(n)

    elif len(n) == 10:
        result = billions(n)
    
    elif len(n) == 11:
        result = ten_billions(n)
    
    elif len(n) == 12:
        result = hundred_billions(n)

    else:
        raise AttributeError('please enter a smaller number')
            
    return result

