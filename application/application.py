
from calendar_lib.constants import print_options, TEMPLATE_FILE
from calendar_lib.year import Year
from calendar_lib.calendar import Calendar, three_calendars
from html.html_gen import HTMLPage
from html.helpers import div_tag
from sys import argv


class IncorrectFormatForYear(BaseException):
    """
    Exception raised if unfamiliar input supplied in place of a year
    """
    pass


class NoCLIArgs(BaseException):
    """
    Exception raised if no CLI args are supplied
    """
    pass


def parse_year(arg: str) -> int:
    """
    Parses CLI year argument and returns Year object if possible
    """
    try:
        year = int(arg)
        if year < 1582:
            raise ValueError
        else:
            return year
    except ValueError as e:
        raise IncorrectFormatForYear
    return

def write_calendars(yr: int, out: str) -> None:
    three_calendars(yr).gen_html(TEMPLATE_FILE, out, yr)

def run() -> None:
    """"Application logic receives CLI arguments and writes calendar for given year to given filepath"""
    if len(argv) >= 3:
        yr = parse_year(argv[1])
        out = argv[2]
        print("Generating calendars for {}, {}, and {}, writing to {}".format(yr-1, yr, yr+1, out))
        write_calendars(yr, out)
        print("Calendars generated")
    else:
        print_options()

