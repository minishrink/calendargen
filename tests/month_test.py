
from calendar_lib.constants import MONTH_LIST
from calendar_lib.month import Month, month_length
from random import randint

def unit_test_month_length(i: int, expected: bool) -> bool:
    assert month_length(i) == expected

def test_month_length() -> None:
    for month in range(12):
        if month == 1:
            unit_test_month_length(month, 28)
        elif month in [3, 5, 8, 10]:
            unit_test_month_length(month, 30)
        else:
            unit_test_month_length(month, 31)

def unit_test_month_name(m: Month, expected) -> None:
    assert m.get_name == expected

def test_month_name() -> None:
    for i in range(12):
        m = Month(i, randint(0,6), randint(1583, 2000))
        unit_test_month_name(m, MONTH_LIST[i].capitalize())

def unit_test_final_week(m: Month, expected) -> None:
    assert m.final_week_complete() == expected

def test_final_week() -> None:
    for m in [0, 2, 4, 6, 7, 9, 11]:
        unit_test_final_week(Month(6, 4, randint(1583,4000)), True)
    # February starting on a Monday, outside of a leap year
    unit_test_final_week(Month(1, 0, randint(1997,1999)), True)
    # February starting on any other day
    for m in range(6):
        unit_test_final_week(Month(1, (m+1), randint(1997,1999)), False)

