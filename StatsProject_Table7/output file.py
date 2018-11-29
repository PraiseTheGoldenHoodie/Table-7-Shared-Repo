import datetime

output_name = input('what is the desired output file name? ')

header = 'File name:',file_name+'.'+file_type,'Output file name:',output_name+'.txt','Username:',username,'Date and time:',datetime.datetime.now()

print(stats_string(x,y)) # prints all stats, only y if it exists


print('x values    y values') # TODO ALSO ALIGN
for i in range(len(data_x)): # TODO FIXME PLEASE HELP ALIGN LEFT AND RIGHT
    print(data_x[i],data_y[i])