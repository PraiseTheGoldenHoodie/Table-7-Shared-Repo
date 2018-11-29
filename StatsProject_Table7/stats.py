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
    varience
    standard_dev
    min
    max
    range
    count
    sum
"""
print("stats imported")
def mean(list):
    total = 0
    for i in list :
        total += i
    avg = total / len(list)
    return avg

def median(list):
    min = list[0]
    for i in list :
        if list[i] < min :
            min = list[i]
    middle = round(len(list) / 2)
    median = list[middle]
    return median

def mode(list):
    """
    TODO: this docstring
    """
    raise NotImplementedError
    return float

def variance(list):
    summ = 0
    for val in list:
        summ = summ + ((float(list[val]) - mean(list)) ** 2)
    var_val = summ / len(list)
    return  var_val

def standard_dev(list):
    """
    TODO: this docstring
    """
    raise NotImplementedError
    return float

def min(list):
    min_val = 9*(10**1000)
    for i in list:
        if i < list[list.index(i) - 1] and i < min_val:
            min_val = i
    return min_val

def max(list):
    max_val = 0
    for i in list:
        if i > list[list.index(i) - 1] and i > max_val:
            max_val = i
    return max_val

def range(list):
    change = max(list) - min(list)
    return change

def count(list):
    """
    TODO: this docstring
    """
    raise NotImplementedError
    return int

def sum(list):
    """
    TODO: this docstring
    """
    raise NotImplementedError
    return int
