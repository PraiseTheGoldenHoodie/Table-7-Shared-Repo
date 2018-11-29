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
    """
    TODO: this docstring
    """
    raise NotImplementedError
    return float

def standard_dev(list):
    """
    TODO: this docstring
    """
    raise NotImplementedError
    return float

def min(list):
    """
    TODO: this docstring
    """
    raise NotImplementedError
    return float

def max(list):
    """
    TODO: this docstring
    """
    raise NotImplementedError
    return float

def range(list):
    """
    TODO: this docstring
    """
    raise NotImplementedError
    return float

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
