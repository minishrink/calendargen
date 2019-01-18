from calendar_lib.constants import TEMPLATE_FILE
from calendar_lib.calendar import three_calendars
from html.html_gen import HTMLPage
from os import remove
from os.path import exists

OUTPUT_DIR="tests/pages"

def delete_file(year) -> None:
    """
    Remove file for given year if it exists, bubble exceptions to toplevel
    """
    try:
        filename = "{}/{}.html".format(OUTPUT_DIR, year)
        if exists(filename):
            remove(filename)
    except OSError as o:
        print("Could not delete file")
        raise o

def compare_code(year: int) -> None:
    try:
        # pregenerated = "../examples/{}.html".format(year)
        pregenerated = "examples/{}.html".format(year)
        # text of pregenerated HTML file
        with open(pregenerated, 'r') as f:
            expected = f.read()
        output_location = "{}/{}.html".format(OUTPUT_DIR, year)
        three_calendars(year).gen_html(TEMPLATE_FILE, output_location, year)
        print("File generated")
        # text of test generated file
        with open(output_location, 'r') as g:
            actual = g.read()
        assert actual == expected
    except IOError as i:
        print("Error: could not read file")
        raise i
    except Exception as e:
        raise e

def test_pages() -> None:
    """
    Test pregenerated pages for given years against test-generated code
    """
    for year in [1800,1900,2000,2017]:
        compare_code(year)
        delete_file(year)
