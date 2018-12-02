def save_menu():
    global unsaved_changes
    # TODO: FIXME: finish this
    output_name = input('what is the desired output file name?\n> ')
    output_file = open(output_name+'.txt')
    output_file.write('Input file name:',inputfile.file_name + OUR_FILE_EXTEN,' |||  Output file name:', output_name + '.txt',' |||  Username:', username,' |||  Date and time:', datetime.datetime.now())
    #print(header)
    #print(stats_strings(data_x, data_y if num_columns() == 2 else None))
    for i in range(stats.count(data_x)):
        output_file.write(data_x[i],data_y[i], sep=',')
    unsaved_changes = False
    pause()