
# CALENDAR GENERATION TOOL

### Prerequisites:
- python3
- pytest (can install by running `pip3 install pytest`, which in turns requires `pip3` installed)

#### Optional:
- Make (this way you can invoke the tool through Make commands)

## Use:
You may use this tool by either directly invoking the `main.py` file, or by running equivalent `Make` commands.

To generate a calendar, enter into the commandline:
  `python3 main.py <YEAR> <DESTINATION>`
Make equivalent:
  `make YEAR=<YEAR> DEST=<DESTINATION>`

  (Note: <DESTINATION> is optional and will default to "generated/<YEAR>.html")

e.g. to generate a file containing calendars for the years 1772, 1773, and 1774:
  `python3 main.py 1773 testfile.html`
or
  `make YEAR=1773`

## Tests:
To run tests:
  `pytest`
or equivalently,
  `make test`

