# Gigasecond

#Write a program that will calculate the date that someone turned or will celebrate their 1 Gs anniversary.
#A gigasecond is one billion (10**9) seconds.

from datetime import datetime
from datetime import timedelta

def add_gigasecond(start):
    return start + timedelta(seconds=(10**9))