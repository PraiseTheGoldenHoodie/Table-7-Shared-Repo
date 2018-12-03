# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:            Alexander Bockelman
#                   Jose Carrillo
#                   Patrick Chai
#                   Jackson Sanders
# Section:          211
# Assignment:       Python Statistics Project
# Date:             2 12 2018

"""
Ladies and gentlemen, welcome to the show. In this category 5 hurricane of a program, you're going to have the
most wonderful pleasure of entering or importing data and doing lots and lots of stuff with it. That stuff 
consists of analyzing many a statistical data, throwing your data into several types of graphs, and writing everything
you do onto a file... just to name a few. We hope you have just as much fun using our program as we did designing it. 
"""
import datetime
import sys
try:
    from . import inputfile, stats, graph
except ImportError:
    try:
        import inputfile, stats, graph
    except ImportError:
        print("That's not how you import this module!")
        import sys
        sys.exit()
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
            assert user_choice < stats.count(selection_pairs)
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
    funcs = ["mean", "median", "mode", "variance", "standard_dev", "min", "max", "range2"]
    right_width = 6  # number of characters for value on right side of equals sign
    left_width = 12
    dec_prec = 2  # number of decimal places
    column_padding = 8*" "  # between x and y columns
    # the following lines evaluate each func (e.g. "mean" becomes stats.mean(x)), with the func's name and result put into formatted string.
    for func in funcs:
        #output += "{:{lw}} = {:>{rw}.{dp}f}".format(func, eval("stats."+func+"(x)"), lw=left_width, rw=right_width, dp=dec_prec)
        output += "x {:{lw}} = {:>{rw}.{dp}f}".format(func, eval("stats."+func+"(x)"), lw=left_width, rw=right_width, dp=dec_prec)
        if y != None:
            output += column_padding + "y {:{lw}} = {:>{rw}.{dp}f}".format(func, eval("stats."+func+"(y)"), lw=left_width, rw=right_width, dp=dec_prec)
        output += "\n"
    # count, the only integer, needs ever so slightly differnt format string.
    output += "x {:{lw}} = {:>{rw}d}".format("count", stats.count(x), lw=left_width, rw=right_width)
    if y != None:
        output += column_padding + "y {:{lw}} = {:>{rw}d}".format("count", stats.count(x), lw=left_width, rw=right_width)
    output += "\n"
    return output

def num_columns():
    """returns how many columns of data this set has, 0 if no data yet."""
    if data_x == None:
        if data_y == None:
            return 0
        else:
            raise ValueError("X values are missing but y values are initialized!")
    else:
        if data_y == None:
            return 1
        else:
            return 2
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
    
    print("I hope you have an excellent day")
    sys.exit()

def save_menu():
    """
    This is the menu that asks for the name of the function then how you would like to save it. Will spit back any errors you
    you have while trying to save it too, with no respect for your dignity
    """
    global unsaved_changes
    if num_columns() == 0:
        print("No data to save!")
        return
    while True:
        output_name = input('what is the desired output file name?\n> ')
        try:
            with open(output_name+'.txt', "w") as output_file:
                output_file.write('Input file name: '+inputfile.file_name + OUR_FILE_EXTEN+'  |||  Output file name: '+ 
                output_name + '.txt |||  Username: '+ username +'  |||  Date and time: '+ str(datetime.datetime.now()) + '\n')
                output_file.write(stats_strings(data_x, data_y if num_columns() == 2 else None) + '\n')
                for i in range(stats.count(data_x)):
                    if num_columns() == 1:
                        output_file.write(str(data_x[i]))
                    else:
                        output_file.write(str(data_x[i])+','+str(data_y[i]))
                    output_file.write("\n")
            unsaved_changes = False
            print("File successfully saved")
            break
        except OSError as err:
            print("Unable to save:", err)
            if not prompt_yes_no("Would you like to retry saving?"):
                break


def load_menu():
    """User loads data from file"""
    global data_x, data_y
    if num_columns() != 0:
        if not prompt_yes_no("You already have data loaded in this session. If you proceed, existing data will be discarded, and new data will be loaded. \nDo you wish to proceed?"):
            return
    input_xy = inputfile.inputfile()
    if input_xy == None:
        return
    data_x, data_y = input_xy

def add_data_menu():
    """user enters data manually"""
    global data_x, data_y, unsaved_changes
    single_column = num_columns() == 1
    prior_data_len = 0
    if num_columns() == 0:  # no data yet
        single_column = choose_submenu("Enter one or two columns?", [("One",True),("Two",False),("Back",None)])
        if single_column == None:  # user selected cancel
            return       
    else:
        prior_data_len = stats.count(data_x)
    if single_column:
        data_x = []
        while True:
                try:
                    x = (input("enter value (or 'q' to quit)\n> "))
                    if x == 'q':
                        break
                    else:
                        data_x.append(float(x))
                except ValueError:
                    print("Value not recognized, enter only numbers")
    else:
        data_x = []
        data_y = []
        while True:
                try:
                    x = input("enter x value (enter 'q' to quit)\n> ")
                    if x == 'q':
                        break 
                    x = float(x)
                    y = float(input("enter corresponding y value (enter 'q' to quit)\n> "))
                    data_x.append(x)
                    data_y.append(y)
                except ValueError:
                    print("Value not recognized, enter only numbers")
    if stats.count(data_x) == prior_data_len:  # No changes made
        if prior_data_len == 0:  # No data
            data_x = None
            data_y = None
    else:
        unsaved_changes = True


def username_menu():
    """Set username"""
    global username
    username = input("Enter new username:\n> ")
    print("username set to", username)
    pause()

def stats_menu():
    """Prints statistic data to console, option for user to save data 
    to file immediately (same save feature on main menu)"""
    global data_x, data_y
    if num_columns() == 2:
        print(stats_strings(data_x, data_y))
    elif num_columns() == 1:
        print(stats_strings(data_x))
    else:
        print("No data to analyze! Choose 'Load data' or 'Add data'.")
        return
    # TODO: asks user if they want to save, and does so if so.

def graph_menu():
    """
    Asks user what graph they want, shows it, save as jpeg.
    """
    if num_columns() == 0:
        print("No data to graph! Choose 'Load data' or 'Add data'.")
        return
    choose_submenu("What type of graph would you like?", [("Histogram", histogram_menu), ("XY Plot", plot_menu), ("Back", back)]) ()

def histogram_menu():
    """
    Brings up the histogram menu and has the user input the settings for which they would like to see their data in a histogram
    """
    if num_columns() == 1:
        graph.histogram(username, data_x, prompt_yes_no("Would you like to save as .jpeg?"))
    else:
        result = choose_submenu("Which data would you like to graph?", [("X-values", False),("Y-values", True),("Both",None)])
        if result == None:
            graph.histogram_subplots(username, data_x, data_y, prompt_yes_no("Would you like to save as .jpeg?"))
        else:
            graph.histogram(username, data_x, prompt_yes_no("Would you like to save as .jpeg?"), is_data_for_y=result)

def plot_menu():
    """
    This asks the user which kind of plot they would like to put their data in
    """
    if num_columns() != 2:
        print("Cannot plot data with only 1 variable!")
        return
    sorted_x, sorted_y = stats.sort(data_x, data_y)
    choose_submenu("What type of X-Y plot?", [("Linear", graph.linear),("Semi-Log(x)", graph.semi_logx),("Semi-Log(y)", graph.semi_logy),
    ("Log-Log", graph.loglog),("All of the above on one figure", graph.plot_subplots)]) (username, sorted_x, sorted_y, prompt_yes_no("Would you like to save as .jpeg?"))
 
################## Begin Execution #####################

# Initialize variables
username = "user"
unsaved_changes = False
data_x = None
data_y = None
OUR_FILE_EXTEN = ".txt"
inputfile.file_name = "keyboard input"

# Main Menu
while True:
    t =  num_columns() != 0
    choose_submenu("----------\nMain Menu\n----------",[
        ("Save data", save_menu),
        ("Load data {}".format("(Data loaded from "+inputfile.file_name+")" if t else "(No data loaded)") , load_menu),
        ("Add data", add_data_menu),
        ("Set username (Current Username: [{}])".format(username), username_menu),
        ("Show statistics", stats_menu),
        ("Create graph", graph_menu),
        ("Quit {}".format("(You have unsaved changes)" if unsaved_changes else ""), quit_menu)]) ()
