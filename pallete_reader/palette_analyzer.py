
import csv
selected_file = 'E:\\MDA\\Beta Testing\\Scripting\\Python\\pallete_reader\\source\\857feb80_6dd8_63e6ab68_1f3de_Palette_menkar_R2023.csv'

with open (selected_file, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader, None)
    temp_list = []
    data_dict = dict()
    for i, row in enumerate(csvreader):
        if row[1] != '' and len(temp_list) == 0:
            temp_list.append([row[2], row[3], i+1])
            data_dict[row[1]] = temp_list
        elif row[1] == '':
            temp_list.append([row[2], row[3], i+1])
        else:
            temp_list = []
            temp_list.append([row[2], row[3], i+1])
            data_dict[row[1]] = temp_list
            
print(data_dict)




