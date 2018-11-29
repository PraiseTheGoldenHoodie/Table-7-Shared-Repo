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

def mean(list):
    """
    :param list: list of data that'll be used to find mean
    :return: mean value as a float
    """
    total = 0
    for i in list :
        total += i
    avg = total / count(list)
    return avg

def median(list):
    """
    :param list: list of data that'll be used to find median
    :return: median value as an int
    """
    if count(list) % 2 != 0 :
        middle = floor(count(list) / 2)
        return middle
    else :
        upper = count(list) / 2
        lower = upper - 1
        middle = (upper + lower) / 2
        return middle

def mode(alist):
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
    freq = max(modes.values())
    for key, val in modes.items():
        if freq == val:
            mode_val.append(key)
    if len(mode_val) > 1:
        mode_val = tuple(mode_val)
    else:
        mode_val = int(mode_val[0])
    return mode_val

def variance(list):
    """
    :param list: list of data that'll be used to find the variance
    :return: variance as a float
    """
    summ = 0
    for val in list:
        summ += ((float(val) - mean(list)) ** 2)
    var_val = summ / len(list)
    return  var_val

def standard_dev(list):
    """
    :param list: list of data that'll be used to find the standard deviation
    :return: standard deviation as a float value
    """
    from math import sqrt
    std_dev = sqrt(variance(list))
    return std_dev

def min(list):
    """
    :param list: list of data that'll be used to find the minimum value of the list
    :return: minimum value in the form of an integer
    """
    min_val = 9*(10**1000)
    for i in list:
        if i < list[list.index(i) - 1] and i < min_val:
            min_val = i
    return min_val

def max(list):
    """
        :param list: list of data that'll be used to find the standard deviation
        :return: maximum value in the form of an integer
    """
    max_val = 0
    for i in list:
        if i > list[list.index(i) - 1] and i > max_val:
            max_val = i
    return max_val

def range(list):
    """
    :param list: list of data that'll be used to find the range
    :return: range value in the form of a float
    """
    change = max(list) - min(list)
    return change

def count(list):
    """
    :param list: list of data that'll be used to find the amount characters in the list
    :return: integer value indicating the number of characters
    """
    counter = 0
    for i in list :
        counter += 1
    return counter

def sum(list):
    """
    :param list: list of data that'll be used to find the sum of all the numbers located in the list
    :return: float value of the sum of all the list's values
    """
    summ = 0
    for i in list :
        summ += i
    return summ

list = [21.3,7,89,1,6,4,8,123,6,8,1,4,68,8,6,8,8,8,1,8,7,4,9,21]

print(mean(list))
print(median(list))
print(mode(list))
print(variance(list))
print(standard_dev(list))
print(min(list))
print(max(list))
print(range(list))
print(count(list))
print(sum(list))