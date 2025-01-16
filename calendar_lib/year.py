
from calendar_lib.constants import leap, WEEKDAYS, MONTH_LIST
from calendar_lib.month import Month
from html.html_gen import Table, HTMLPage
from html.helpers import div_tag, newlines, tag_data
from typing import List

def leap_between(x: int, y: int) -> int:
    f = lambda x : x//4 - x//100 + x//400
    diff = f(y) - f(x)
    return int(diff)

def leap_years_between(x: int, y: int) -> int:
    count = 0
    for year in range(x, y):
        if leap(year):
            count += 1
    return count

def year_starts_on(year: int) -> int:
    """
    Given a year X => 1582, return the weekday of Jan 1st X
    """
    leap_years = leap_years_between(1583, year)
    # leap_years = leap_between(1583, year)
    years = (year - 1583)
    # add offset because 1583 started on a Saturday = WEEKDAYS[5]
    difference = (leap_years + years + 5)
    return difference % 7


class Year(object):
    """"
    Class to create a year-long calendar
    """

    def __init__(self, year: int, start_m: int = 0, end_m: int = 11):
        """
        Create a Year object, autoinitialised with 12 months
        """
        self._year = year
        self._first = year_starts_on(year)
        self._start_m = min(start_m, end_m)
        self._end_m = max(start_m, end_m)

    def __repr__(self):
        return "Year({self._year}, {self._first}, {self._start_m}, {self._end_m)".format(self=self)

    def __str__(self):
        return "Year({}, {}, {}, {})".format(
            self._year, WEEKDAYS[self._first].capitalize(), MONTH_LIST[self._start_m], MONTH_LIST[self._end_m]
            )

    @property
    def first_day(self) -> int:
        return self._first

    @property
    def start_month(self) -> int:
        return self._start_m

    @property
    def end_month(self) -> int:
        return self._end_m

    @property
    def year_num(self) -> int:
        return self._year
