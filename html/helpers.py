
from typing import List

# HTML table constants
HTML = "html"
HD = "head"
TBL = "table"
TBL_D = "td"
TBL_H = "th"
TBL_R = "tr"
CAPTION = "caption"


def newlines(lines : List[str]) -> str:
    return ('\n'.join(lines))

def tag_data(tag: str, data: str, tag_cls: str = None, sep: str = '') -> str:
    """

    data: string to wrap
    tag:  tag to wrap string
    sep:  separator string (ie newline) between tags and data
    Returns data wrapped in given tag
    """
    if tag_cls is None:
        cls_str = ""
    else:
        cls_str = " class=\"{}\"".format(tag_cls)
    if data is not None:
        return "<{0}{1}>{3}{2}{3}</{0}>".format(tag, cls_str, data, sep)
    else:
        return ""


# function typing?
def tag_fn(tag: str) -> object:
    """

    :param tag: HTML tag T
    :return: function tag_T(data: str) which calls tag_data(T, data)
    """

    docs = """
    :param data: string to wrap in {0} tag
    :return <{0}>data</{0}>
    """.format(tag)

    def tag_f(data: str, tag_cls: str = None, sep: str = ''):
        return tag_data(tag, data, tag_cls, sep)
    tag_f.__doc__ = docs
    return tag_f


# table
tbl = tag_fn(TBL)

# table headers
tbl_h = tag_fn(TBL_H)

# table rows
tbl_r = tag_fn(TBL_R)

# table data
tbl_d = tag_fn(TBL_D)

# table caption
cpt = tag_fn(CAPTION)

def div_tag(div_cls, data) -> str:
    """

    div_cls: name of div class
    data:    data to wrap in div
    Returns data wrapped in div class
    """
    return ("<div class=\"{}\">\n{}\n</div>\n".format(div_cls, data))
