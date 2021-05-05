import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
from suntime import Sun, SunTimeException

def get_start_date():
    m = int(input("Please enter starting month: "))
    y = int(input("Please enter starting year: "))
    return [m, y]

def get_end_date():
    m = int(input("Please enter ending month: "))
    y = int(input("Please enter ending year: "))
    return [m, y]

def get_starting_info():    
    latitude = float(input("Please enter latitude: "))
    longitude = float(input("Please enter longtitude: "))
    power = int(input("Please enter installation power: "))

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

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
        monthlyUsage[f"{currentMonth}.{currentYear}"] = calculate_monthly_usage(*args, currentYear, currentMonth)
        if not (currentMonth != endDate[0] or currentYear != endDate[1]):
            break
        if currentMonth < 12:
            currentMonth += 1
        else:
            currentMonth = 1
            currentYear += 1
    return monthlyUsage

def get_usage_in_period(start_date, end_date):
    monthly_usage = {}
    current_month = start_date[0]
    current_year = start_date[1]
    while True:
        monthly_usage[f"{current_month}.{current_year}"] = float(input(f"Usage for {current_month}.{current_year}: "))
        #months -= 1
        if not (current_month != end_date[0] or current_year != end_date[1]):
            break
        if current_month < 12:
            current_month += 1
        else:
            current_month = 1
            current_year += 1
    return monthly_usage

if __name__ == '__main__':
    plt.style.use("seaborn-dark")

    latitude = 51.11163
    longitude = 17.05367
    power = 55
    startTime = [1, 2020]
    endTime = [6, 2020]

    """
    latitude, longtitude, power = get_starting_info()
    startTime = get_start_date()
    endTime = get_end_date()
    """

    given_usage_for_period = get_usage_in_period(startTime, endTime)
    predictedUsageForPeriod = calculate_usage_in_period(startTime, endTime, latitude, longitude, power)
    print("---------------------------------------------------")
    print(f"Start date: {startTime[0]}.{startTime[1]}")
    print(f"End date: {endTime[0]}.{endTime[1]}")
    for i in predictedUsageForPeriod:
        print(f"Date: {i} || Predicted: {predictedUsageForPeriod[i]} kWh")
    print("---------------------------------------------------")

    x = np.arange(len(predictedUsageForPeriod))
    fig, ax = plt.subplots(figsize=(12  ,6))
    bars_width = 0.4
    predicted_bar = ax.bar(x - bars_width/2, predictedUsageForPeriod.values(), bars_width, label="Calculated usage")
    given_bar = ax.bar(x + bars_width/2, given_usage_for_period.values(), bars_width, label="Given usage")
    ax.set_xlabel("Dates")
    ax.set_xticks(x)
    ax.set_xticklabels(predictedUsageForPeriod.keys())
    ax.set_ylabel("Energy usage [kWh]")
    ax.legend()
    ax.bar_label(predicted_bar, padding=3)
    ax.bar_label(given_bar, padding=3)
    plt.show()
