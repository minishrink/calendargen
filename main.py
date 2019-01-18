from application.application import run, IncorrectFormatForYear
from calendar_lib.constants import leap, print_options

def main() -> None:
    """
    Validate CLI args and generate calendar, print menu otherwise
    """
    try:
        run()
    except IncorrectFormatForYear:
        print("Year must be an integer > 1582")
    except Exception as e:
        print_options()
        raise e

if (__name__=="__main__"):
    main()
