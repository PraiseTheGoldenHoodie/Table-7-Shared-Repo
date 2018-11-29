import matplotlib.pyplot as plt

#x = [1,10,100]
#y = [1,10,100]

def histogram(list):
    ''' function histogram takes in a list, returns a histogram of the values in the list, plot has title and axes. '''
    bins = int(len(list)/2)
    plt.hist(list,bins = bins, color = 'maroon')
    plt.title('histogram data plot')
    plt.xlabel('data types')
    plt.ylabel('data frequency')
    plt.show()

def linear(xlist,ylist):
    ''' function linear takes in a x data list and y data list, and returns a linear plot with a title and axes '''
    plt.plot(xlist,ylist,color = 'maroon')
    plt.title('linear data plot')
    plt.xlabel('x data values')
    plt.ylabel('y data values')
    plt.show()

def semi_logx(xlist,ylist):
    ''' function semi_logx takes in a x data list and a y data list, and returns a plot with log x as x axis, and a normal y axis '''
    plt.semilogx(xlist,ylist,color = 'maroon')
    plt.title('semi-log x data plot')
    plt.xlabel('log x data values')
    plt.ylabel('y data values')
    plt.show()

def semi_logy(xlist,ylist):
    ''' function semi_logy takes in a x data list and a y data list, and returns a plot with log y as y axis, and a normal x axis '''
    plt.semilogy(xlist,ylist,color = 'maroon')
    plt.title('semi-log y data plot')
    plt.xlabel('x data values')
    plt.ylabel('log y data values')
    plt.show()

def loglog(xlist,ylist):
    ''' function loglog takes in a x data list and a y data list, and returns a plot with both log x and log y as its axes '''
    plt.loglog(xlist,ylist,color = 'maroon')
    plt.title('log log plot of data values')
    plt.xlabel('log x data values')
    plt.ylabel('log y data values')
    plt.show()

def subplots(xlist,ylist):
    ''' function subplots combines the linear, semi_logx, semi_logy, and loglog plots into one subplot with the four plots '''
    # linear graph
    plt.figure(1)
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
    plt.show()

#subplots(x,y)
#plt.savefig('dataplot.jpg')
