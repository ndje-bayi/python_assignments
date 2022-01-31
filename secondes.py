"""
This program prompts the user to enter a number of seconds; then it breaks it down into years, months, weeks, minutes
and seconds then finaly prints the result

"""
#The scale of seconds
SECONDS_IN_YEAR = 31536000
SECONDS_IN_MONTH = 2592000
SECONDS_IN_WEEK = 604800
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def main():
    seconds = input("Enter the number of seconds: >>> ")
    if seconds.isdecimal():
        result = break_down(seconds)
        print("""The number of years is: {}\nThe number of months is: {}\nThe number of weeks is: {}\
            \nThe number of days is: {}\nThe number of hours is: {}\nThe number of minutes is: {}\
            \nThe number of seconds is: {}""".format(result[0],
            result[1], result[2], result[3], result[4], result[5], result[6]))
        
    else:
        print(seconds, "is an invalid input")
        

def break_down(seconds):
    seconds = int(seconds)
    years = int(seconds / SECONDS_IN_YEAR)
    remaining = seconds % SECONDS_IN_YEAR
    months = int(remaining / SECONDS_IN_MONTH)
    remaining %= SECONDS_IN_MONTH
    weeks = int(remaining / SECONDS_IN_WEEK)
    remaining %= SECONDS_IN_WEEK
    days = int(remaining / SECONDS_IN_DAY)
    remaining %= SECONDS_IN_DAY
    hours = int(remaining / SECONDS_IN_HOUR)
    remaining %= SECONDS_IN_HOUR
    minutes = int(remaining / SECONDS_IN_MINUTE)
    seconds = remaining % SECONDS_IN_MINUTE
    return years, months, weeks, days, hours, minutes, seconds

if __name__ == "__main__":
    main()