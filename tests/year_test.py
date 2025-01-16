
from typing import Callable
from calendar_lib.year import leap_years_between, year_starts_on, Year

def unit_test_leap_years_between(x: int, y: int, expected: int) -> None:
    assert leap_years_between(x,y) == expected

def test_leap_years_between() -> None:
    unit_test_leap_years_between(1600, 1600, 0)
    unit_test_leap_years_between(1600, 1601, 1)
    unit_test_leap_years_between(1600, 1604, 1)
    unit_test_leap_years_between(1600, 1605, 2)
    # final year should not be included
    unit_test_leap_years_between(1600, 1696, 24)
    # ensure multiples of 4 between 100s are counted regardless
    unit_test_leap_years_between(1600, 1697, 25)
    # ensure multiples of 100 only count if they are multiples of 400
    unit_test_leap_years_between(1600, 1700, 25)
    # check for normal behaviour after a century
    unit_test_leap_years_between(1600, 1701, 25)
    unit_test_leap_years_between(1600, 1703, 25)
    unit_test_leap_years_between(1600, 1704, 25)
    unit_test_leap_years_between(1600, 1705, 26)

def unit_test_year_starts_on(y: int, expected: int) -> None:
    assert year_starts_on(y) == expected

def test_year_starts_on() -> None:
    # hardcoded dates as verified by Wikipedia
    unit_test_year_starts_on(1583, 5)
    unit_test_year_starts_on(1600, 5)
    unit_test_year_starts_on(1700, 4)
    unit_test_year_starts_on(1800, 2)
    unit_test_year_starts_on(1900, 0)

def unit_test_year_getters(Y: Year, y: int, first: int, start: int = 0, end: int = 11) -> None:
    assert Y.first_day == first
    assert Y.start_month == start
    assert Y.end_month == end
    assert Y.year_num == y

def test_year_getters() -> None:
    unit_test_year_getters(Year(1582, 9, 11), 1582, 4, 9, 11)
    unit_test_year_getters(Year(1583), 1583, 5)
    unit_test_year_getters(Year(1599), 1599, 4)
    unit_test_year_getters(Year(1600), 1600, 5)
    unit_test_year_getters(Year(1601), 1601, 0)
