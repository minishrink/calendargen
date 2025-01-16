from calendar_lib.constants import leap, MONTH_LIST, WEEKDAYS, WEEKDAYS_ABBREV, NOT_IN_MONTH
from html.html_gen import Table, HTMLPage
from html.helpers import cpt


def month_length(month: int, leap_year: bool = False):
    """
    Calculate length of given month
    """
    if month == 1:
        # handle February
        return 28 + int(leap_year)
    elif month in [3, 5, 8, 10]:
        return 30
    else:
        return 31

class Month(object):
    """
    Create an object representing calendar months
    """

    def __init__(self, month_num: int, first_day: int, year: int):
        """
        Creates a Month object starting on specified day
        """
        self._n_days = month_length(month_num, leap(year))
        self._month = month_num
        self._start = first_day
        self._year = year

    @property
    def name(self) -> str:
        """
        Return name of month
        """
        return MONTH_LIST[self._month].capitalize()

    @property
    def len(self) -> int:
        """
        Return number of days in month
        """
        return self._n_days

    @property
    def first(self) -> int:
        """
        Return weekday by number 0-6 for Monday-Sunday
        """
        return self._start

    @property
    def first_day(self) -> str:
        """
        Return weekday by name
        """
        return WEEKDAYS[self._start].capitalize()

    def __repr__(self):
        return "Month({}, {}, {})".format(self._month, self._start, self._year)

    def __str__(self):
        return "Month({self.name}, {self.first_day}, {self._year})".format(self=self)

    @property
    def num_weeks(self) -> int:
        """
        Return how many weeks (Monday - Sunday) the month stretches over
        i.e. how many rows required in the calendar
        """
        if self.len + self.first > 35:
            return 6
        elif self.len + self.first > 28:
            return 5
        else:
            return 4

    def final_week_complete(self) -> bool:
        """
        Check if calendar table for month fills entire bottom row
        """
        return ((self._n_days + self.first) % 7) == 0

    def make_table(self, week_offset: int) -> str:
        """
        Generate HTML table
        """
        start = 1
        # Hardcode beginning of Gregorian calendar on 15/10/1582
        if self._year == 1582 and self._month == 9:
            start = 15

        def display(day):
            """
            Text representation of date
            """
            if day < start or day > (self._n_days):
                return NOT_IN_MONTH
            else:
                return '{:>2}'.format(day)

        caption="{} {}".format(self.name, self._year)
        # weekday banner
        week_hdrs = ["#"] + WEEKDAYS_ABBREV
        weeks = [
                # week numbers
                ['{:>2}'.format(str(j + 1 + week_offset))] +
                # WEEKDAYS
                [display(i + ((j << 3) - j)) for i in range(1 - self._start, 8 - self._start)]
                for j in range(self.num_weeks)
                ]
        return Table(caption, div_name="month", headers=week_hdrs, rows=weeks)
