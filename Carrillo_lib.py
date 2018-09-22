# Here are some functions I wrote you all might find useful.
# To use them, make sure Carrillo_lib is in your working directory. Then call
# import Carrillo_lib
#  or
# from Carrillo_lib import *


def xd_contains(xd_list, item):
    """checks any-dimensional list to see if it contains an item. Item can be any type except list."""
    if type(xd_list) is not list:
        return xd_list == item
    else:
        for row in xd_list:
            if xd_contains(row, item):
                return True
        return False


def box_formatter(in_strings, horizontal_line="-", whole_horizontal_line=False, side_decor="", corner_decor="", alignment=0):
    """Takes list of text lines and puts them in a customizable box. Returns one string with UNIX EOL characters."""
    bar = horizontal_line
    in_strings_len = []
    for i in range(len(in_strings)):
        in_strings_len.append(len(in_strings[i]))
    bar *= max(in_strings_len) // len(horizontal_line)  # integer repeats of line_char
    if whole_horizontal_line:
        bar += horizontal_line  # tack an extra set on, have some slack
    else:
        bar += horizontal_line[:max(in_strings_len) % len(horizontal_line)]  # cut off at longest line
#    bar = corner_decor + bar + corner_decor
    lines = ""

    if alignment == -1:
        alignment = ".ljust(len(bar))"
    elif alignment == 1:
        alignment = ".rjust(len(bar))"
    else:
        alignment = ".center(len(bar))"

    corner_padding = max(0, len(side_decor) - len(corner_decor))
    side_padding = max(0, len(corner_decor) - len(side_decor))

    for line in in_strings:
        line = eval("line"+alignment)
        line = (side_padding * ' ') + side_decor + line + side_decor + (' ' * side_padding)
        lines += line+'\n'
    bar = (corner_padding * ' ') + corner_decor + bar + corner_decor + (' ' * corner_padding)
    result = bar + '\n' + lines + bar
    return result


def yes_no(prompt):
    """Returns boolean user response. Repeats question until they give valid input."""
    prompt = prompt.lower()
    while True:
        response = input(prompt)
        if response == "y" or response == "yes" or response == "ye" or response == "yep" or response == "yeah" or response == "yea":
            return True
        if response == "n" or response == "no" or response == "nope" or response == "hell no" or response == "fuck off":
            return False
        print("Input not recognized, type either 'y' or 'n'")


