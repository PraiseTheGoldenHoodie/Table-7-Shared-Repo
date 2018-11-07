# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 	Alexander Bockelman
#           Jose Carrillo
# 	 		Patrick Chai
# 	 		Jackson Sanders
# Section:		211
# Assignment:	lab 11a-1 
# Date:		7 11 2018

import math

def F(x):
    y = x**2 - 1
    y = math.sin((math.e)**x) + math.pi
    return y    

def deriv(x):  #aka F'(x)
    a = 9**-9
    top = F(x + a) - F(x)
    bot = a
    slope = top / bot
    return slope

def newton_step(xi):
    d  = deriv(xi)
    if d == 0:  # we hit the root dead-on
        return xi  # avoids divide-by-zero
    x = xi - F(xi)/deriv(xi)
    return x 
def newton(x0):  # returns list of steps converging towards a root.
    # if it diverges, gets stuck in an infinite root.
    approxes = []
    while True:
        x = newton_step(x0)                    
        if abs(x-x0) <= 10**-6:
            break
        approxes.append(x0)
        x0 = x
    return approxes        

# part e
print("Newton:", newton(float(input("Initial guess? xo ="))))
