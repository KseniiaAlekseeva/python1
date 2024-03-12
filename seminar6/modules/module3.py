import datetime as dt
import calendar

__all__=['check_date']

def check_date(date_string: str) -> bool:
    form = "%d.%m.%Y"
    try:
        data = dt.datetime.strptime(date_string, form)
        print(data)
        print('Leap = ',check_year(data.year))
        return True
    except:
        return False

def check_year(year:int)->bool:
    return calendar.isleap(year)