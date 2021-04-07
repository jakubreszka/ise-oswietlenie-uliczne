import datetime
from suntime import Sun, SunTimeException

latitude = 51.21
longitude = 21.01

def calculate_usage(lat, lon, y, m, d):
    """
    Calculates sunrise and sunset at specified location in specified date
    """
    date_sun = Sun(lat, lon)
    time = datetime.date(year=y, month=m, day=d)
    date_sunrise = date_sun.get_local_sunrise_time(time)
    date_sunset = date_sun.get_local_sunset_time(time)
    return (date_sunrise, date_sunset)

test_sr, test_ss = calculate_usage(latitude, longitude, 2020, 5, 12)
print(f"Sunrise at test: {test_sr.hour:02d}:{test_sr.minute:02d}, sunset at test: {test_ss.hour:02d}:{test_ss.minute:02d}")

"""
CODE EXAMPLES FROM PACKAGE

sun = Sun(latitude, longitude)

# Get today's sunrise and sunset in UTC
today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()
print('Today at Warsaw the sun raised at {} and get down at {} UTC'.
      format(today_sr.strftime('%H:%M'), today_ss.strftime('%H:%M')))

# On a special date in your machine's local time zone
abd = datetime.date(2014, 10, 3)
abd_sr = sun.get_local_sunrise_time(abd)
abd_ss = sun.get_local_sunset_time(abd)
print('On {} the sun at Warsaw raised at {} and get down at {}.'.
      format(abd, abd_sr.strftime('%H:%M'), abd_ss.strftime('%H:%M')))

# Error handling (no sunset or sunrise on given location)
latitude = 87.55
longitude = 0.1
sun = Sun(latitude, longitude)
try:
    abd_sr = sun.get_local_sunrise_time(abd)
    abd_ss = sun.get_local_sunset_time(abd)
    print('On {} at somewhere in the north the sun raised at {} and get down at {}.'.
          format(abd, abd_sr.strftime('%H:%M'), abd_ss.strftime('%H:%M')))
except SunTimeException as e:
    print("Error: {0}.".format(e))
"""
