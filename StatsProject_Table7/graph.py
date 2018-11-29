import matplotlib.pyplot as plt


def histogram(list):
    bins = int(len(list)/2)
    plt.hist(list,bins = bins, color = 'maroon')
    plt.title('histogram data plot')
    plt.xlabel('data types')
    plt.ylabel('data frequency')
    plt.show()

def linear(xlist,ylist):
    plt.plot(xlist,ylist,color = 'maroon')
    plt.title('linear data plot')
    plt.xlabel('x data values')
    plt.ylabel('y data values')
    plt.show()

def semi_logx(xlist,ylist):
    plt.semilogx(xlist,ylist,color = 'maroon')
    plt.title('semi-log x data plot')
    plt.xlabel('log x data values')
    plt.ylabel('y data values')
    plt.show()

def semi_logy(xlist,ylist):
    plt.semilogy(xlist,ylist,color = 'maroon')
    plt.title('semi-log y data plot')
    plt.xlabel('x data values')
    plt.ylabel('log y data values')
    plt.show()

def loglog(xlist,ylist):
    plt.loglog(xlist,ylist,color = 'maroon')
    plt.title('log log plot of data values')
    plt.xlabel('log x data values')
    plt.ylabel('log y data values')
    plt.show()

def subplots(xlist,ylist):
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

subplots(x,y)