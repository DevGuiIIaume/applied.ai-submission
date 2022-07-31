import sys
import math
from datetime import date as true_date

class Date:
    def __init__(self, year: int, month: int, day: int, date: str) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.date = date

def calculate_true_difference(first_date: Date, second_date: Date) -> int:
    """Uses the datetime library to calculate the true value between two dates"""

    true_first_date = true_date(first_date.year, first_date.month, first_date.day)
    true_second_date = true_date(second_date.year, second_date.month, second_date.day)

    # Determine the difference
    true_difference = true_first_date - true_second_date

    return abs(true_difference.days) - 1

def get_julian_day_number(date_object: Date) -> int:
    """Converts the Gregorian calendar date into its Julian day number
    Reference: https://www.researchgate.net/publication/316558298_Date_Algorithms
    """

    year = date_object.year
    month = date_object.month
    day = date_object.day

    # We consider March as month 1, which greatly simplifies leap year calculations
    if month < 3:
        month += 12
        year -= 1

    days_in_prev_months = int((153 * month - 457)/5)
    days_in_a_year = 365 * year
    days_considering_leap_years = math.floor(year / 4) - math.floor(year / 100) \
                                    + math.floor(year / 400)
    jdn_offset = 1721119

    # Calculate the julian day number
    julian_day_number = day + days_in_prev_months + days_in_a_year + \
                        days_considering_leap_years + jdn_offset

    return julian_day_number

def calculate_difference(first_date: Date, second_date: Date) -> int:
    """Calculates the difference in days between two date objects"""

    first_jdn = get_julian_day_number(first_date)
    second_jdn = get_julian_day_number(second_date)

    return abs(first_jdn - second_jdn) - 1

def is_valid_format(date: str) -> bool:
    """Checks that the date is in the correct format i.e. YYYY-MM-DD"""

    if 10 != len(date):
        # Check that the date is the correct length
        print("Error: the length of the date is not valid")
        return False
    if ('-' != date[5]) and ('-' != date[7]):
        # Check that the separators are correct and in the right location
        print("Error: the separators are either not correct or in the wrong location")
        return False
    if not (date[0:4].isnumeric() and date[5:7].isnumeric() and date[8:10].isnumeric()):
        # Check that YYYY, MM, and DD are numeric
        print("Error: the dates are not all numeric")
        return False

    return True

def is_valid_day(date_object: Date) -> bool:
    """Returns false if the day is less than or equal to zero"""

    return date_object.day > 0

def is_valid_month(date_object: Date) -> bool:
    """Checks that the month is within 1 and 12 inclusive"""

    return (date_object.month >= 1 and date_object.month <= 12)

def is_leap_year(year: int) -> bool:
    """Returns true if the year is a leap year, otherwise false"""

    if ((0 == year % 4) and (0 != year % 100)) or (0 == year % 400):
        return True
    else:
        return False

def is_valid_day_in_month(date_object: Date) -> bool:
    """Checks whether the day-month pair is valid"""

    # If we are given the 29th of February, check that it is a leap year
    if (29 == date_object.day) and (2 == date_object.month):
        if is_leap_year(date_object.year):
            return True
        else:
            return False

    months_with_30_days = [4, 6, 9, 11]
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]

    # Check that the day given is valid given the month
    if (date_object.day <= 28) and 2 == date_object.month:
        return True
    elif (date_object.day <= 30 and date_object.month in months_with_30_days):
        return True
    elif (date_object.day <= 31 and date_object.month in months_with_31_days):
        return True
    else:
        return False

def is_valid_year(date_object: Date) -> bool:
    """Returns false if the year is less than or equal to zero"""

    return date_object.year > 0

def is_valid_date(date: str) -> bool:
    """Checks that the date is valid eg. no 30th of February"""

    date_object = init_date_object(date)

    if not is_valid_year(date_object):
        print("Error: the year is not valid")
        return False
    if not is_valid_month(date_object):
        print("Error: the month is not valid")
        return False
    if not is_valid_day(date_object):
        print("Error: the day is not valid")
        return False
    if not is_valid_day_in_month(date_object):
        print("Error: the (day, month) pair is not valid")
        return False

    return True

def init_date_object(valid_date: str) -> Date:
    """Initialise a Date object given a valid date string"""

    year = int(valid_date[0:4])
    month = int(valid_date[5:7])
    day = int(valid_date[8:10])

    return Date(year, month, day, valid_date)

def get_date() -> Date:
    """Get the date from stdin"""

    while True:
        date = input("Please provide a valid date in the format YYYY-MM-DD: ")

        # Accept the input only if it is a valid format and valid date
        if is_valid_format(date) and is_valid_date(date):

            return init_date_object(date)


def main() -> None:

    # Get the dates from stdin
    first_date = get_date()
    second_date = get_date()

    difference = calculate_difference(first_date, second_date)

    print(f"The difference between {first_date.date} and {second_date.date} is {difference} days")

if __name__ == "__main__":
    main()
