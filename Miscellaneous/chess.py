def create_square(light=True):
    """This function creates a square on the board by creating an HTML td tag with class='light' if `light` is set to True else class='dark' defining a light and dark square respectively."""
    return f"<td class=\"{'light' if light else 'dark'}\"></td>\n"


def create_row(columns:int, light_first=True):
    """This function creates one row by creating `columns` number of columns and wrapping them in an HTML tr tag.
    `light_first` is a boolean value which determines if the first cell should have a class='light' otherwise class='dark'
    :return: str"""
    output = ""
    for i in range(columns):    # starts the loop to create the columns on the row
        output += create_square(light_first)
        light_first = not(False or light_first)     # switches the `light` variable to make the next square a dark one
    return f"<tr>\n{output}</tr>\n"


def create_board(rows:int, columns:int, light_first:bool=True, to_html:bool=False):
    output = ""
    for i in range(rows):
        output += create_row(columns, light_first)
        light_first = not(False or light_first)
    table_snippet = f"<table>\n{output}\n</table>\n"
    if not to_html:
        return table_snippet
    with open('board.html', 'w') as fp:
        fp.write(table_snippet)