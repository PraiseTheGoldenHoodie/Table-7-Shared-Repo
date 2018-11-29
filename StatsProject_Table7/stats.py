# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names: 	Alexander Bockelman
#           Jose Carrillo
# 	 		Patrick Chai
# 	 		Jackson Sanders
# Section:		211
# Assignment:	Python Statistics Project
# Date:		24 11 2018
"""
Module that contains all statistic functions defined for this package.

functions:
    mean
    median
    mode
    variance
    standard_dev
    min
    max
    range
    count
    sum
"""

print("stats imported")

def mean(alist):
    """
    :param alist: alist of data that'll be used to find mean
    :return: mean value as a float
    """
    total = 0
    for i in alist :
        total += i
        # Running sum
    avg = total / count(alist)
    # Sum divided by the amount of characters in the alist to find the mean
    return avg

def median(alist):
    """
    :param alist: list of data that'll be used to find median
    :return: median value as an int
    """
    if count(alist) % 2 != 0 :
    # Determines if the length of the list is odd. If it is, then it returns the value in the direct middle of the list
        middle = count(alist) // 2
        return middle
    else :
    # This means the length of the list is even and it takes the average of the two central numbers of the list
        upper = count(alist) / 2
        lower = upper - 1
        middle = (upper + lower) / 2
        return middle

def mode(alist):  # FIXME: doesn't work when I've tried it
    """
    :param alist: list of data that will be used to find mode
    :return: mode_val as an integer if more than one mode returns as tuple
    """
    modes = {}
    mode_val = []
    for i in alist:
        if i in modes:
            modes[i] += 1
        else:
            modes[i] = 1
    freq = max(list(modes.values()))
    for key, val in modes.items():
        if freq == val:
            mode_val.append(key)
    if len(mode_val) > 1:
        mode_val = tuple(mode_val)
    else:
        mode_val = int(mode_val[0])
    return mode_val

def variance(alist):
    """
    :param alist: list of data that'll be used to find the variance
    :return: variance as a float
    """
    summ = 0
    for val in alist:
        summ += ((float(val) - mean(alist)) ** 2)
    var_val = summ / len(alist)
    # This is the variance formula. Riveting.
    return  var_val

def standard_dev(alist):
    """
    :param alist: list of data that'll be used to find the standard deviation
    :return: standard deviation as a float value
    """
    from math import sqrt
    std_dev = sqrt(variance(alist))
    # It's just the square root of the variance
    return std_dev

def min(alist):
    """
    :param alist: list of data that'll be used to find the minimum value of the list
    :return: minimum value in the form of an integer
    """
    min_val = 9*(10**1000)
    # Big ol number to start as max so it'll run, then anything smaller will turn into min
    for i in alist:
        if i < alist[alist.index(i) - 1] and i < min_val:
            min_val = i
    return min_val

def max(alist):
    """
        :param alist: list of data that'll be used to find the standard deviation
        :return: maximum value in the form of an integer
    """
    max_val = 0
    # Same thing as the min func except this time it finds the biggest number
    for i in alist:
        if i > alist[alist.index(i) - 1] and i > max_val:
            max_val = i
    return max_val

def range(alist):
    """
    :param alist: list of data that'll be used to find the range
    :return: range value in the form of a float
    """
    change = max(alist) - min(alist)
    # It is what it is
    return change

def count(alist):
    """
    :param alist: list of data that'll be used to find the amount characters in the list
    :return: integer value indicating the number of characters
    """
    counter = 0
    for i in alist :
        counter += 1
    # Simple way of finding how many characters are in the list without an inbuilt function
    return counter

def sum(alist):
    """
    :param alist: list of data that'll be used to find the sum of all the numbers located in the list
    :return: float value of the sum of all the list's values
    """
    summ = 0
    for i in alist :
        summ += i
    # Adds each term in the list to a sum variable as the loop iterates through the list, finding the summation
    return summ

# Available to test a list if the user so desires
# print(mean(list))
# print(median(list))
# print(mode(list))
# print(variance(list))
# print(standard_dev(list))
# print(min(list))
# print(max(list))
# print(range(list))
# print(count(list))
# print(sum(list))