# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Alexander Bockelman
#       Jackson Sanders
#       Patrick Chai
#       Jose Carrillo
# Section: 211
# Assignment: Lab 7a- Activity 2
# Date: October 9 2018
from math import*

first_round = []
sec_round = []
name = []
n=0

#takes in first round and second round scores and names
while n>=0:
    first = input("what was the first round score? ")
    first = int(first)
    if first < 0:
        print("scores accepted")
        break
    else:
        first_round.append(first)
    second = input("what was the second round score? ")
    second = int(second)
    sec_round.append(second)
    names = input("what is the golfer's name? ")
    name.append(names)
    n+=1
    print("------------------------------------")

sum_scores = [0]

sum_scores = [first_round[i]+ sec_round[i] for i in range(len(name))]
#sums first round and second round scores

#makes copy of sum_scores
sum_scores1 = sum_scores.copy()


sort_fround = first_round
sort_sround = sec_round
sort_name = name
store = 0

#sorts all scores into ascending order, in new list called sum_scores1
for x in range(1,len(sum_scores1)):
    store = sum_scores[x]
    position = x
    while position>0 and store<sum_scores1[position-1]:
        sum_scores1[position] = sum_scores1[position-1]
        position = position-1
    sum_scores1[position] = store
#sum_scores1 is sorted list

winner = []
loser = []

#the median is the cutoff score
if len(sum_scores1)%2==0:
    median = (sum_scores1[int(len(sum_scores1)/2-1)]+sum_scores1[int((len(sum_scores1)/2))])/2
else:
    median = (sum_scores1[int(floor(len(sum_scores1)/2))]+sum_scores1[int(ceil((len(sum_scores1)/2)))])/2


for j in range(0,len(name)):
    if sum_scores[j] <= median:
        winner.append(name[j])
    if sum_scores[j] > median:
        loser.append(name[j])
print("----------------------------------------------")
print("golfers moving on are ",winner)
print("----------------------------------------------")
print("golfers who are now cut out are ",loser)