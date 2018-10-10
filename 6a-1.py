# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Alexander Bockelman
#       Jackson Sanders
#       Patrick Chai
#       Jose Carrillo
# Section: 211
# Assignment: Lab 6a- Activity 1
# Date: October 3 2018
start_point = input("what is the start point? ")
start_point = float(start_point)
end_point = input("what is the end point? ")
end_point = float(end_point)
A = input("what is the A coefficient? ")
A = float(A)
B = input("what is the B coefficient? ")
B = float(B)
C = input("what is the C coefficient? ")
C = float(C)
D = input("what is the D coefficient? ")
D = float(D)

m = 0 # Dummy variable
fa = 0 # Also can be read as f(a)
fb = 0 # Also can b read as f(b)
fm = 0 # f(m)

i = 0
while end_point-start_point<=10**-7:
    fa = A*(start_point)**3+B*(start_point)**2+C*(start_point)+D
    fb = A*(end_point)**3+B*(end_point)**2+C*(end_point)+D
    m = (start_point+end_point)/2
    fm = A*m**3+B*m**2+C*m+D
    if fm <0:
        start_point=m
    else:
        end_point=m
    i += 1
    if i >= 10**7:
        print("Infinite loop detected! Quitting early...")
        break
print((start_point+end_point)/2)
