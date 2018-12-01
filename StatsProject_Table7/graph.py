import matplotlib.pyplot as plt
import datetime
from PIL import Image
from os import remove



#x = [1,10,100]
#y = [1,10,100]

def histogram(username, alist, save_picture, is_data_for_y=False):
    ''' function histogram takes in a list, returns a histogram of the values in the list, plot has title and axes. 
    :is_data_for_x: is a Boolean that specifies if data is from x or y, so that file can be saved with correct figure number'''
    bins = int(len(alist)/2)  # FIXME: better algrorithm is needed, especially for data with 100,000+ points
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
    if save_picture:
        savefig_as_jpeg(username, 6)
    plt.show()

def histogram_subplots(username, xlist, ylist, save_picture):
    # TODO: plot histograms of x and y values side-by-side
    if save_picture:
        savefig_as_jpeg(username, 6)
    plt.show()



def savefig_as_jpeg(username, figure_number):
    plt.savefig("temp.png", format="png") # matplotlib cannot save as jpeg
    temp_png = Image.open("temp.png","r") # RGBA format
    png = temp_png.convert("RGB")  # drop alpha channel
    file_name = "{}_{}_Fig_{}.jpeg".format(username, datetime.datetime.now().date().isoformat(), figure_number)
    png.save(file_name)
    remove("temp.png")


#subplots(x,y)
#plt.savefig('dataplot.jpg')
