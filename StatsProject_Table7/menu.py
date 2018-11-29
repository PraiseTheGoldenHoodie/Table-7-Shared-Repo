# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:     Alexander Bockelman
#            Jose Carrillo
#             Patrick Chai
#             Jackson Sanders
# Section:        211
# Assignment:    Python Statistics Project
# Date:        28 11 2018
"""
TODO: this docstring
"""
print("menu imported")
import graph
import stats
import datetime

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

def enumerate_options(prompt, choices):
    """
    Displays prompt with enumerated choices, returns index of choice user selects.
    Repeats if invalid user response.

    prompt (string)
    choices (index) """
    while True:
        print(prompt)
        i = 0  # define i in this scope so we can use it later
        for choice in choices:
            i += 1
            print("{:2}) {}".format(i, choice))
        try:
            user_choice = input("> ").strip()
            user_choice = int(user_choice)
            assert user_choice < len(choices) + 1
            return user_choice - 1  # -1 to convert to zero index
        except (ValueError, AssertionError):  # User enters something that's not an int, or User enters invalid number
            print("'%s' not valid selection, type a number between 1 and %d"%(user_choice, i))
            pause()
    
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


##############################################"mode", 
############# BEGIN EXECUTION ################
##############################################

username = "user"  #TODO: extract username from file
unsaved_changes = False

data_x = None
data_y = None
include_y = None

while True:
    c1 = enumerate_options("----------\nMain Menu\n----------",[
        "Save data",
        "Load data",
        "Add data", 
        "Set username (Current Username: [{}])".format(username),
        "Show statistics",
        "Create graph",
        "Quit {}".format("(You have unsaved changes)" if unsaved_changes else "")])
    if c1 == 0:  # SAVE
        print("Do save function here")
        # TODO: FIXME: finish this
        output_name = input('what is the desired output file name? ')
        header = 'File name:',file_name+'.'+file_type,'Output file name:',output_name+'.txt','Username:',username,'Date and time:',datetime.datetime.now()
        print(stats_string(x,y)) # prints all stats, only y if it exists
        for i in range(len(data_x)):
            print(data_x[i],data_y[i], sep=',')
        unsaved_changes = False
        pause()
    if c1 == 1:   # LOAD
        data_x = [1,2,5,6]
        data_y = [9, 6, 1, 10]
        include_y = True
    if c1 == 2:  # ADD
        #TODO:
        pass
    if c1 == 3:  # USERNAME
        username = input("Enter new username:\n> ")
        print("username set to",username)
        pause()
    if c1 == 4:  # STATS
        print(stats_strings(data_x))
        print(stats_strings(data_x, data_y))
        pass
    if c1 == 5:  # GRAPH
        print("You are about to plot your data, please enter the corresponding keyword to choose which type of display: ")
        c2 = enumerate_options("What type of plot would you like?", ["Histogram","Linear","Semi_logx","Semi_logy","LogLog","Subplots"])
        # TODO: all the other options, such as when include_y is false
        if c2 == 0:    # HISTOGRAM
            if include_y:
                c3 = enumerate_options("Choose dataset to plot:", ["x","y"])
                if c3 == 0:
                    graph.histogram(data_x)
                if c3 == 1:
                    graph.histogram(data_y)
            else:
                graph.histogram(data_x)
        if c2 == 1:
            graph.linear(data_x, data_y)
        if c2 == 2: 
            graph.semi_logx(data_x, data_y)
        if c2 == 3:
            graph.semi_logy(data_x, data_y)
        if c2 == 4: 
            graph.loglog(data_x, data_y)
        if c2 == 5:
            graph.subplot(data_x, data_y)

    if c1 == 6: # QUIT # FIXME
        if unsaved_changes:
            if not prompt_yes_no("Exit without saving?"):
                continue
        break
