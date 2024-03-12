import datetime as dt
import calendar
from sys import argv

__all__ = ['check_date']


def check_date(date_string=None) -> bool:
    if date_string is None:
        args = [i for i in argv[1:]]
        if len(args) < 1:
            print('Not enough arguments')
        else:
            date_string = args[0]
            pass
        print(args)

    form = "%d.%m.%Y"
    try:
        data = dt.datetime.strptime(date_string, form)
        print(data)
        print('Leap = ', check_year(data.year))
        return True
    except:
        return False


def check_year(year: int) -> bool:
    return calendar.isleap(year)
