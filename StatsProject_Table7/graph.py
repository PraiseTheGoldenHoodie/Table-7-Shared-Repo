# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:            Alexander Bockelman
#                   Jose Carrillo
#                   Patrick Chai
#                   Jackson Sanders
# Section:          211
# Assignment:       Python Statistics Project
# Date:             5 12 2018

import matplotlib.pyplot as plt
import datetime
try:
    from . import stats
except ImportError:
    try:
        import stats
    except ImportError:
        print("That's not how you import this module!")
        import sys
        sys.exit()

# Here are some example lists if you're too lazy to come up with your own
# x = [1,10,100]
# y = [1,10,100]

def histogram(username, alist, save_picture, is_data_for_y=False):
    ''' 
    function histogram takes in a list, returns a histogram of the values in the list, plot has title and axes. 
    :is_data_for_x: is a Boolean that specifies if data is from x or y, so that file can be saved with correct figure number
    '''
    bins = int(stats.count(alist)/10)
    bins = stats.min((bins, 50))
    bins = stats.max((bins, 5))
    plt.hist(alist,bins = bins, color = 'maroon')
    plt.title("%s data" % ("y" if is_data_for_y else "x"))
    plt.xlabel('value')
    plt.ylabel('frequency')
    if save_picture:
        savefig_as_jpeg(username, int(is_data_for_y))  # figure 0 or 1 for x or y respectively
    plt.show()

def linear(username, xlist, ylist, save_picture):
    ''' function linear takes in a x data list and y data list, and returns a linear plot with a title and axes '''
    plt.plot(xlist,ylist,color = 'maroon')
    plt.title('linear data plot')
    plt.xlabel('x data values')
    plt.ylabel('y data values')
    if save_picture:
        savefig_as_jpeg(username, 2)
    plt.show()

def semi_logx(username, xlist, ylist, save_picture):
    ''' function semi_logx takes in a x data list and a y data list, and returns a plot with log x as x axis, and a normal y axis '''
    plt.semilogx(xlist,ylist,color = 'maroon')
    plt.title('semi-log x data plot')
    plt.xlabel('log x data values')
    plt.ylabel('y data values')
    if save_picture:
        savefig_as_jpeg(username, 3)
    plt.show()

def semi_logy(username, xlist, ylist, save_picture):
    ''' function semi_logy takes in a x data list and a y data list, and returns a plot with log y as y axis, and a normal x axis '''
    plt.semilogy(xlist,ylist,color = 'maroon')
    plt.title('semi-log y data plot')
    plt.xlabel('x data values')
    plt.ylabel('log y data values')
    if save_picture:
        savefig_as_jpeg(username, 4)
    plt.show()

def loglog(username, xlist, ylist, save_picture):
    ''' function loglog takes in a x data list and a y data list, and returns a plot with both log x and log y as its axes '''
    plt.loglog(xlist,ylist,color = 'maroon')
    plt.title('log log plot of data values')
    plt.xlabel('log x data values')
    plt.ylabel('log y data values')
    if save_picture:
        savefig_as_jpeg(username, 5)
    plt.show()

def plot_subplots(username, xlist, ylist, save_picture):
    ''' function subplots combines the linear, semi_logx, semi_logy, and loglog plots into one figure with the four subplots '''
    # linear graph
    #plt.figure(1)
    plt.subplot(2,2,1)
    plt.plot(xlist, ylist, color='maroon')
    plt.title('linear data plot')
    plt.xlabel('x data values')
    plt.ylabel('y data values')
    # semi log x graph
    plt.subplot(2,2,2)
    plt.semilogx(xlist, ylist, color='maroon')
    plt.title('semi-log x data plot')
    plt.xlabel('log x data values')
    plt.ylabel('y data values')
    # semi log y graph
    plt.subplot(2,2,3)
    plt.semilogy(xlist, ylist, color='maroon')
    plt.title('semi-log y data plot')
    plt.xlabel('x data values')
    plt.ylabel('log y data values')
    plt.subplot(2,2,4)
    # log log graph
    plt.loglog(xlist, ylist, color='maroon')
    plt.title('log log plot of data values')
    plt.xlabel('log x data values')
    plt.ylabel('log y data values')
    plt.subplots_adjust(hspace=0.6)
    if save_picture:
        savefig_as_jpeg(username, 6)
    plt.show()

def histogram_subplots(username, xlist, ylist, save_picture):
    """This one will print out two histograms, side by side, displaying x's and y's individually"""
    plt.subplot(1,2,1)
    bins = int(stats.count(xlist)/10)
    bins = stats.min((bins, 50))
    bins = stats.max((bins, 5))
    plt.hist(xlist,bins = bins, color = 'maroon')
    plt.title("%s data" % ("x"))
    plt.xlabel('x values')
    plt.ylabel('frequency')

    plt.subplot(1,2,2)
    bins = int(stats.count(ylist)/10)
    bins = stats.min((bins, 50))
    bins = stats.max((bins, 5))
    plt.hist(ylist,bins = bins, color = 'maroon')
    plt.title("%s data" % ("y"))
    plt.xlabel('y values')
    plt.ylabel('frequency')
    if save_picture:
        savefig_as_jpeg(username, 7)
    plt.show()



def savefig_as_jpeg(username, figure_number):
    """
    Wrote this function before I realized that you could do plt.savefig(..., format="jpeg")
    But I spent a lot of time to figure this out, so I'm leaving it
    """
    file_name = "{}_{}_Fig_{}.jpeg".format(username, datetime.datetime.now().date().isoformat(), figure_number)
    try:
        plt.savefig(file_name, format="jpeg")
    except ValueError:
        print("Unabled to save as JPEG, saving as PNG instead.")
        plt.savefig(file_name, format="png")

#subplots(x,y)
#plt.savefig('dataplot.jpg')
