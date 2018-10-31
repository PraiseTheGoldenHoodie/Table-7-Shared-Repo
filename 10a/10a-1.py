# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Alexander Bockelman
#       Jackson Sanders
#       Patrick Chai
#       Jose Carrillo
#
# Section: 211
# Assignment: Lab 10a- Activity 1
# Date: 31 10 2018

#As a team, we have gone through all required sections of the tutorial, and each team member understands the material
import numpy as np

#A = np.zeros((3,4))
A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#B = np.empty((4,2))
B = np.array([[4,2],[2,3],[3,4],[6,9]])
#C = np.ones((2,3))
C = np.array([[4,2,6],[2,3,7]])
D = np.array([[4],[2],[3]])

print(A, B, C, D, sep="\n")

E = A@B@C  # matrix multiplication
#E = A.dot(B.dot(C))  # alternatively
print(E)
print(E.T)  # transpose
print(np.linalg.solve(E.T, D))  #lInaLGerRor: sIngUlAr mATrIx
