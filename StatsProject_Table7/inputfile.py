
file_name = input('what is the file name? ')
file_type = input('what is the file type? (csv, tsv, or txt only) ').lower()
file_type = file_type.strip('.')

# takes in file type, returns file type indicator
def csv_tsv(file_type):
    if file_type == 'csv'.lower():
        return','
    elif file_type == 'tsv'.lower():
        return '\t'
    else:
        return 'stop'

# below is code for text file, appends each line (number) to a list after converting to float
if file_type == 'txt'.lower():
     with open(file_name+'.txt','r') as infile:
        data = infile
        data_x = []
        data_y = []
        # loop through data, check for headers, then strip unnecessary characters from numbers, then convert to floats and into lists
        for line in data:
            if line[0].isnumeric() is True:
                if ',' in line:
                    line = line.split(',')
                    line[0].strip('"')
                    line[1].replace('"', '')
                    line[1].strip('\n')
                    data_x.append(float(line[0]))
                    data_y.append(float(line[1]))
                    include_y = True
                else:
                    include_y = False
                    pass
            else:
                pass

# below is code for csv/tsv file, appends each line(number) to a list after converting to float
elif csv_tsv(file_type) != 'stop':
    with open(file_name+'.'+file_type,'r') as infile:
        data = infile
        data_x = []
        data_y = []
        # strips unnecessary characters from files, then convert to float, then append to list
        for line in data:
            if csv_tsv(file_type) == 'stop':
                break
            elif csv_tsv(file_type) in line:
                line = line.split(csv_tsv(file_type))
                line[0] = line[0].strip('"')
                line[1] = line[1].replace('"','')
                line[1] = line[1].strip('\n')
                data_x.append(float(line[0]))
                data_y.append(float(line[1]))
                include_y = True
            else:
                nums = nums.append(float(line))
                include_y = False

print(data_x)
print(data_y)