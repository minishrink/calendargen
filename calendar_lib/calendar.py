
from typing import List
from calendar_lib.constants import TEMPLATE_FILE
from calendar_lib.year import Year
from calendar_lib.month import Month
from html.html_gen import Table, HTMLPage
from html.helpers import *

class Calendar(object):
    """
    Calendar class takes a year and generates HTML for year calendar
    """

    def __init__(self, y: int):
        self._year = Year(y)
        if y == 1582:
            self._year = Year(1582, start_m=9)

    @property
    def get_year(self) -> Year:
        return self._year

    @property
    def get_year_value(self) -> int:
        return (self._year).get_year_num

    def __repr__(self):
        return "Calendar({})".format(self._year._year)

    def gen_months(self) -> List[Month]:
        """
        Initialise calendar with Month objects
        list of Month objects (with correct week/day offset)
        """
        yr = self._year
        first_day = yr._first
        months = []
        for i in range(yr._start_m, yr._end_m + 1):
            m = Month(i, first_day, yr._year)
            first_day = (first_day + m.get_len) % 7
            months.append(m)
        return months

    def gen_year(self) -> List[Table]:
        """
        Generate static HTML for calendar year
        Returns list of Table objects representing months
        """
        month_tables : List[Table] = []
        offset = 0
        for m in self.gen_months():
            continue_week = not m.final_week_complete()
            month_tables.append(m.make_table(offset))
            offset += (m.num_weeks - int(continue_week))
        return month_tables

    def html_calendar(self) -> str:
        """
        Return static HTML string for given year
        """
        year_banner = tag_data("h1", self.get_year_value)
        months: str = newlines([str(t) for t in self.gen_year()])
        yr_calendar = year_banner + div_tag("year", months)
        return yr_calendar


def three_calendars(yr: int) -> HTMLPage:
    """
    Given year Y, generate HTML for years (Y-1), Y, and (Y+1),
    provided all comply with the Gregorian calendar
    """
    previous_year = tag_data(tag="h3", data="Gregorian calendar available from October 1582")
    if yr > 1582:
        previous_year = Calendar(yr-1).html_calendar()
    current_year = Calendar(yr).html_calendar()
    next_year = Calendar(yr+1).html_calendar()
    return HTMLPage(body='\n'.join([previous_year, current_year, next_year]))

