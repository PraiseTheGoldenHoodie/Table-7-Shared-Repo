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
# Assignment: Lab 7a- Activity 2
# Date: October 9 2018

# User inputs
qscores_unsorted = []  # Qualifying scores, i.e. sum of first two scores. Qualifying scores determine who makes the cut.
names = []  #names of golfers
print("Enter the scores followed by the name of each golfer. Enter -1 as first score after all golfers have been entered.")
while True:
    first = int(input("What was the first round score? (Enter -1 to end) "))
    if first < 0:
        print("Scores accepted.")
        break
    second = int(input("What was the second round score? "))
    qscores_unsorted.append(first+second)
    names.append(input("What is the golfer's name? "))
    print("------------------------------------")

# Sorts all scores into ascending order, in new list called qscores_sorted
# FIXME: IDK how this sort algorithm works, can someone who knows document this? Or at least identify what type it is? 
# It looks like some variant of insertion but for preserving original unsorted list.
qscores_sorted = qscores_unsorted[:]  # makes shallow-copy
store = 0
for x in range(1,len(qscores_sorted)):
    store = qscores_unsorted[x]
    position = x
    while position>0 and store<qscores_sorted[position-1]:
        qscores_sorted[position] = qscores_sorted[position-1]
        position = position-1
    qscores_sorted[position] = store

# Find the median score, which will be used as the cutoff
if len(qscores_sorted)%2 == 0:  # median is average of two middle values if even sized list
    median_upper_index = len(qscores_sorted) // 2
    median = (qscores_sorted[median_upper_index] + qscores_sorted[median_upper_index - 1]) / 2  # Average lower and upper vals around median
else:
    median = qscores_sorted[len(qscores_sorted) // 2]  # works because of zero-indexing

winners = []
losers = []

# Add names who made cutoff to 'winners', those who didn't go to 'losers'
for j in range(0,len(names)):
    if qscores_unsorted[j] <= median:  # We check against qscores_unsorted because it is parallel to names list
        winners.append(names[j])
    else:
        losers.append(names[j])
# Output
print("----------------------------------------------")
print("Golfers moving on:")
for winner in winners:
    print(winner)
print("----------------------------------------------")
print("Golfers that did not make the cut:")
for loser in losers:
    print(loser)
print("----------------------------------------------")
