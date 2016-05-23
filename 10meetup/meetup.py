from datetime import date

import calendar
import itertools

# MeetupDayException

def meetup_day(year, month, day, request):
    '''Takes in a requested week of meetup time (2013, 5, 'Monday', 'teenth') and returns the proper date'''
    
    # [(date, dayWeek)]
    cal = calendar.Calendar()
    myMonth = cal.monthdays2calendar(year, month)
    
    # calculate which tuple to access by day of the week
    dayOfWeek = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }
    requestDay = dayOfWeek[day]
    
    # Make an array of all the dates in the month that fall on the requested day
    allDays = []
    for item in itertools.chain.from_iterable(myMonth):
        if item[1] == requestDay:
            if item[0] != 0:
                allDays.append(item)

    # return the date at the requested week
    if request == '1st':
        requestDate = allDays[0]
    elif request == '2nd':
        requestDate = allDays[1]
    elif request == '3rd':
        requestDate = allDays[2]
    elif request == '4th':
        requestDate = allDays[3]
    elif request == '5th':
        requestDate = allDays[4]
    elif request == 'last':
        requestDate = allDays[len(allDays)-1]
    elif request == 'teenth':
        for (day, dayWeek) in allDays:
            if 10<day<20:
                requestDate = (day, dayWeek)

    # turn the requestDate into a date object
    meetingDate = date(year, month, requestDate[0])

    return meetingDate