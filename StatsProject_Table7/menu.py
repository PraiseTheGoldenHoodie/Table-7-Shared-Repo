# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:     Alexander Bockelman
#            Jose Carrillo
#             Patrick Chai
#             Jackson Sanders
# Section:        211
# Assignment:    Python Statistics Project
# Date:        1 12 2018
"""
TODO: this docstring
"""
print("menu imported")
import datetime
import sys
import graph
import stats

################## Misc Functions #####################
# Any function that isn't a menu goes in this section

def prompt_yes_no(question):
    """
    Asks user yes/no question, returns boolean user response.
    Repeats if invalid user response.

    question (string) - usually ends with question mark. Printed, followed by '[y/n]: '
    """
    while True:
        choice = input( question + " [y/n]\n> ").strip().lower()
        if choice == "y":
            return True
        elif choice =="n":
            return False
        print("'%s' not valid selection, type only y or n"%choice)

def choose_submenu(prompt, selection_pairs):
    """
    Asks the user a multiple choice question, returns the object paired 
    with selected option.
    :prompt: The string above list of choices (Typically the question).
    :selection_pair: 2D iterable (e.g. list of tuples), where:
        each row is a choice,
        column 0 is the string displayed as that choice to the user, and
        column 1 is the object returned if that choice is selected.
    """
    while True:
        print(prompt)
        i = 0  # define i in this scope so we can use it later
        for pair in selection_pairs:
            i += 1
            print("{:2}) {}".format(i, pair[0]))
        try:
            user_choice = input("> ").strip()
            user_choice = int(user_choice)
            user_choice -= 1  # convert to zero index
            assert user_choice < len(selection_pairs)
            return selection_pairs[user_choice][1]
        except (ValueError, AssertionError):  # User enters something that's not an int, or User enters invalid number
            print("'%s' not valid selection, type a number between 1 and %d"%(user_choice, i))

def pause():
    """literally input("[ENTER to continue]"), but just in case we want to change this message"""
    input("[ENTER to continue]\n> ")

def stats_strings(x, y=None):
    r"""
    takes one or two lists of data and returns string (containing \n characters) of all stats functions and their values.
    prints y data as second column to the right of x column.
    """
    output = ""
    funcs = ["mean", "median", "mode", "variance", "standard_dev", "min", "max", "range"]
    right_width = 6  # number of characters for value on right side of equals sign
    left_width = 12
    dec_prec = 2  # number of decimal places
    column_padding = 8*" "  # between x and y columns
    # the following lines evaluate each func (e.g. "mean" becomes stats.mean(x)), with the func's name and result put into formatted string.
    for func in funcs:
        output += "{:{lw}} = {:>{rw}.{dp}f}".format(func, eval("stats."+func+"(x)"), lw=left_width, rw=right_width, dp=dec_prec)
        if y != None:
            output += column_padding + "{:{lw}} = {:>{rw}.{dp}f}".format(func, eval("stats."+func+"(y)"), lw=left_width, rw=right_width, dp=dec_prec)
        output += "\n"
    # count, the only integer, needs ever so slightly differnt format string.
    output += "{:{lw}} = {:>{rw}d}".format("count", stats.count(x), lw=left_width, rw=right_width)
    if y != None:
        output += column_padding + "{:{lw}} = {:>{rw}d}".format("count", stats.count(x), lw=left_width, rw=right_width)
    output += "\n"
    return output

################## Menu Functions #####################
# These menu functions replace the ugly, hard-to-read, hard-to-maintain if-elif-elif-...-else statements
# in controlling navigation between question prompts. They take no parameters, return None, and
# output any changes they have made by declaring the affected variable as 'global'
# be aware not to excede 1,000 menus within menus - this is only a risk if the menu calls itself, or calls
# a menu that calls the first, etc. 
def back():
    """Placeholder function used by other menus calling choose_submenu."""
    return

def quit_menu():
    """Gives save confirmation before exiting program"""
    if unsaved_changes:
        if not prompt_yes_no("Exit without saving?"):
            return
    sys.exit()

def save_menu():
    global unsaved_changes
    # TODO: FIXME: finish this
    output_name = input('what is the desired output file name? ')
    header = 'File name:',file_name+'.'+file_type,'Output file name:',output_name+'.txt','Username:',username,'Date and time:',datetime.datetime.now()
    print(stats_strings(data_x,data_y if single_column else None)) # prints all stats, only y if it exists
    for i in range(len(data_x)):
        print(data_x[i],data_y[i], sep=',')
    unsaved_changes = False
    pause()

def load_menu():
    global data_x, data_y, single_column, unsaved_changes
    ## Manually setting data temporarily, just so I have something to test with
    data_x = [1,2,5,6]  # temporary
    data_y = [9, 6, 1, 10] # temporary
    single_column = True # temporary
    unsaved_changes = True # temporary
    # TODO: actually load data
    # TODO: prompt user whether or override all existing data with data loaded in, or append new data (and if so, make sure the number of columns match)
    # TODO (optional): read username from file name if username still 'user'
    # TODO (optional): 

def add_data_menu():
    """user enters data manually"""
    global single_column, data_x, data_y, unsaved_changes
    if single_column == None:  # no data yet
        single_column = choose_submenu("Enter one or two collums?", [("One",True),("Two",False),("Back",None)])
        if single_column == None:  # user selected cancel
            return
    if single_column:
        pass # TODO
    else:
        pass # TODO
    unsaved_changes = True
    # TODO

def username_menu():
    """Set username"""
    global username
    username = input("Enter new username:\n> ")
    print("username set to", username)
    pause()

def stats_menu():
    """Prints statistic data to console, option for user to save data 
    to file immediately (same save feature on main menu)"""
    global data_x, data_y, single_column
    if data_x == None:
        return
    if single_column:
        print(stats_strings(data_x, data_y))
    else:
        print(stats_strings(data_x))
    # TODO: asks user if they want to save, and does so if so.

def graph_menu():
    """
    Asks user what graph they want, shows it, save as jpeg.
    """
    if data_x == None:
        print("No data to graph! Choose 'Load data' or 'Add data'.")
        return
    graph_func = choose_submenu("What type of graph would you like?", [("Histogram", graph.histogram),
    ("Linear", graph.linear),("Semi-Log(x)", graph.semi_logx),("Semi-Log(y)", graph.semi_logy),
    ("Log-Log", graph.loglog),("Subplots", graph.subplots)])
    if graph_func == graph.histogram:
        if not single_column:
            graph_func(data_x)
        elif choose_submenu("Which data would you like to graph?", [("x-values", True),("y-values", False)]):
            graph_func(data_x)
        else:
            graph_func(data_y)
    else:
        if not single_column:
            args = (range(len(data_x)), data_x)
        else:
            args = (data_x, data_y)
        graph_func(*args)
    #TODO: save as .jpeg



################## Begin Execution #####################

# Initialize variables
username = "user"
unsaved_changes = False
data_x = None
data_y = None
single_column = None

# Main Menu
while True:
    choose_submenu("----------\nMain Menu\n----------",[
        ("Save data", save_menu),
        ("Load data", load_menu),
        ("Add data", add_data_menu),
        ("Set username (Current Username: [{}])".format(username), username_menu),
        ("Show statistics", stats_menu),
        ("Create graph", graph_menu),
        ("Quit {}".format("(You have unsaved changes)" if unsaved_changes else ""), quit_menu)]) ()
