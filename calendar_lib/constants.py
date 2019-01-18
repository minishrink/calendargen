
def leap(year: int) -> bool:
    """
    Given year X >= 1582, returns whether X is a leap year
    """
    # Multiples of 100 must also be of 400
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

def print_options():
    """
    Print CLI menu
    """
    print("\tUsage: python3 main.py [YEAR] [FILE]\n\tYEAR must be an integer larger than 1581")

MONTH_LIST = [ "january",
           "february",
           "march",
           "april",
           "may",
           "june",
           "july",
           "august",
           "september",
           "october",
           "november",
           "december" ]

WEEKDAYS = [ "monday",
             "tuesday",
             "wednesday",
             "thursday",
             "friday",
             "saturday",
             "sunday" ]

WEEKDAYS_ABBREV = [(day[0].upper() + day[1]) for day in WEEKDAYS]
NOT_IN_MONTH = ("{:>2}".format(' '))
TEMPLATE_FILE="html/template.html"

