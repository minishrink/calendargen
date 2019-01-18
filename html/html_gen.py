
from typing import List, Dict   # provide type annotations

from html.helpers import newlines, tbl, tbl_h, tbl_r, tbl_d, cpt, div_tag


class Row(object):
    """
    Class to define HTML table rows
    """

    def __init__(self, data_list: List[str], tbl_fn=tbl_d):
        """
        tag wrapper function for row data (default: tbl_d)
        Takes list of data objects and wraps them in provided tag
        """
        self._data = data_list
        self._tbl_fn = tbl_fn

    def __repr__(self):
        return "Row({self._data})".format(self=self)

    def __str__(self):
        """
        HTML for table row
        """
        # wrap week number in td class
        _rows = [tbl_d(self._data[0], tag_cls='week_n')] + \
                ["{}".format(self._tbl_fn(d)) for d in self._data[1:]]
        row_str = newlines(_rows)
        return tbl_r(row_str, sep='\n')


class Table(object):
    """
    Class to define HTML tables and encapsulate table data
    """

    def __init__(self, caption: str, div_name: str, headers: List[str], rows: List[List[str]]):
        self._caption = caption
        self._div = div_name
        self._headers = headers
        self._rows = rows

    def __repr__(self):
        return "Table({self._caption}, {self._div}, {self._headers}, {self._rows}".format(self=self)

    def __str__(self):
        cap = cpt(self._caption)
        hdrs = str(Row(self._headers, tbl_h))
        rows = newlines([str(Row(row)) for row in self._rows])
        table = tbl(newlines([cap, hdrs, rows]), sep='\n')
        div = div_tag(self._div, table)
        return div

class HTMLPage(object):
    """
    Static HTML object class
    """

    def __init__(self, body: str):
        """
        body: page contents string
        Returns static HTML page string
        """
        self._body = body

    def __repr__(self):
        return "HTMLPage(body = {self._body}".format(self=self)

    def __str__(self):
        return self._body

    @staticmethod
    def find_replace(from_file: str, to_file: str, replacements: Dict[str, str]) -> None:
        """
        from_file: path of file to read from
        to_file: path of file to write in
        replacements: Map of strings to find and replace
        """
        # read template file into string, perform replacements and then write to destination file
        # in order to minimise file access time
        try:
            with open(from_file, 'r') as f:
                src = f.read()
            for placeholder in replacements.keys():
                src = src.replace(("{{ % _{}_ % }}".format(placeholder.upper())), replacements[placeholder])
            with open(to_file, 'w') as dest:
                dest.write(src)
        except Exception as e:
            raise e

    def gen_html(self, from_path: str, to_path: str, yr: int) -> None:
        """
        from_path: filepath to read from
        to_path: filepath to write to (default: from_path)
        """
        replacements = {'title': "{} - {}".format(yr-1, yr+1), 'data': self._body}
        HTMLPage.find_replace(from_path, to_path, replacements)
