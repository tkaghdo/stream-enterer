__author__ = 'Tamby Kaghdo'

import datetime

def day(date):
    return datetime.date(int(date[:4]),int(date[4:6]),int(date[6:])).strftime("%A")

print(day("20160301"))



