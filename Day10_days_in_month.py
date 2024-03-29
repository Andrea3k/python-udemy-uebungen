# function for returning days for a special year and month

def is_leap(year):
    if year % 4 == 0: 
        if year % 100 == 0: 
            if year % 400 == 0: 
                is_leap = True
            else: 
                is_leap = False
        else: 
            is_leap = True
    else: 
        is_leap = False
    return is_leap


year = int(input("Please enter a year: \n"))
month = int(input("please enter a month: \n"))

leap_year = is_leap(year)

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = is_leap(year)
    if leap_year == True and month == 2: 
        days = month_days[1] + 1
        return days 
    else: 
        days = month_days[month - 1]
        return days 

days = days_in_month(year, month)

print(f"the {month}. month of {year} has {days} days.")