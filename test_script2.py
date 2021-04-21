import datetime, timedelta
from suntime import Sun, SunTimeException

latitude = 51.11163
longitude = 17.05367
power = 50
startTime = [1, 2020]
endTime = [12, 2020]

# A function to determine if a year is a leap year.
# Do not change this function.
def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

# You should complete the definition of this function:

def days_in_month(month, year):
    if month in [9, 4, 6, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2 and is_leap_year(year) == True:
        return 29
    elif month == 2 and is_leap_year(year) == False:
        return 28
    else:
        return None

def calculate_monthly_usage(lat, lon, power, y, m):
    """
    Calculates sunrise and sunset at specified location in specified date
    """
    daysInMonth = days_in_month(m, y)
    totalMonthlyUsage = 0
    for i in range(daysInMonth):
        date_sun = Sun(lat, lon)
        time = datetime.date(year=y, month=m, day=i + 1)
        date_sunrise = date_sun.get_local_sunrise_time(time)
        date_sunset = date_sun.get_local_sunset_time(time)
        total_hours = datetime.timedelta(hours = 24) - (date_sunset - date_sunrise)
        totalMonthlyUsage += ((total_hours.total_seconds()) / 3600) * power
    return round(totalMonthlyUsage, 2)

def calculate_usage_in_period(startDate, endDate, *args):
    monthlyUsage = {}
    currentMonth = startDate[0]
    currentYear = startDate[1]
    while True:
        monthlyUsage[str(currentMonth) + "." +
                     str(currentYear)] = calculate_monthly_usage(
                         *args, currentYear, currentMonth)
        if not (currentMonth != endDate[0] or currentYear != endDate[1]):
            break
        if currentMonth < 12:
            currentMonth += 1
        else:
            currentMonth = 1
            currentYear += 1
    return monthlyUsage

predictedUsageForPeriod = calculate_usage_in_period(startTime, endTime, latitude, longitude, power)
print("---------------------------------------------------")
print("Start date: " + str(startTime[0]) + "." +
                     str(startTime[1]))
print("End date: " + str(endTime[0]) + "." +
                     str(endTime[1]))
for i in predictedUsageForPeriod:
  print("Date: " + str(i) + " || Predicted power usage: " + str(predictedUsageForPeriod[i]) + " kWh")
print("---------------------------------------------------")

def calculate_daily_usage(lat, lon, power, y, m, d):
  """
  Calculates sunrise and sunset at specified location in specified date
  """
  date_sun = Sun(lat, lon)
  time = datetime.date(year=y, month=m, day=d)
  date_sunrise = date_sun.get_local_sunrise_time(time)
  date_sunset = date_sun.get_local_sunset_time(time)
  total_hours = date_sunset - date_sunrise
  return ((total_hours.total_seconds()) / 3600) * power

#print(calculate_daily_usage(latitude, longitude, power, 2020, 1, 3))
#print(calculate_daily_usage(latitude, longitude, power, 2020, 7, 1))