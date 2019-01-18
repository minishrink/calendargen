
from calendar_lib.constants import leap

def unit_test_leap(year: int, expected: bool) -> None:
    """Assert given year is or is not a leap year"""
    assert leap(year) == expected

def test_leap() -> None:
    """Run unit tests for leap year"""
    for i in range(1804,1897, 4):
        unit_test_leap(i, True)
    for i in range(1600, 4000, 100):
        unit_test_leap(i, (i % 400) == 0)
    for i in range(1700, 2000, 100):
        unit_test_leap(i, False)
