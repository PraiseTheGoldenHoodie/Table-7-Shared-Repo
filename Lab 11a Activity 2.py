values =        [1,2,3,4,5,6,7,8,9]
measurement = [0,1,2,3,4,5,6,7,8]
query = 0
max = -9**9
min = 9**9

for i in range(0,len(measurement)):
    if measurement[i]>max:
        max = measurement[i]
    if measurement[i] < min:
        min = measurement[i]


top = (query - values[0])*(measurement[len(measurement)-1]-measurement[0])
bottom = values[len(values)-1] - values[0]
y = top/bottom + measurement[0]
print(y)
