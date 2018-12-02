print("inputfile imported")
def csv_tsv(file_type):
    """takes in file type, returns file type indicator"""
    if file_type == 'csv':
        return ','
    elif file_type == 'tsv':
        return '\t'
    else:
        return 'stop'


file_name = "no file"
def inputfile():
    global file_name
    while True:
        raw_in = input("Enter file path (or enter 'c' to cancel):\n> ").strip()
        if raw_in.lower() == "c":
            break
        raw_in = raw_in.rsplit('.',1)
        if len(raw_in) != 2:
            print("Invalid file path, must include an extension (e.g. '.txt')")
            continue
        file_name, file_type = raw_in
        print(file_name, file_type)
        try:
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
                                try:
                                    x = float(line[0])
                                    y = float(line[1])
                                    data_x.append(x)
                                    data_y.append(y)
                                except ValueError:
                                    continue
                            else:
                                data_x.append(float(line))
                                data_y = None
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
                            try:
                                data_x.append(float(line[0]))
                                data_y.append(float(line[1]))
                            except ValueError:  # skip unreadable lines
                                continue
                        else:
                            data_x.append(float(line))
                            data_y = None
                    if len(data_x) == 0:
                        print("No readable data in file")

            return data_x, data_y
        except OSError as err:
            print(err)

#inputfile()