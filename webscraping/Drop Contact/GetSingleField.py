# import csv
# csv_file_path = './new_new_data.csv'
# column_index = 21
# data_dict=dict()
# with open(csv_file_path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader, None)
#     for row in csv_reader:
#         value = row[column_index]
#         if value.strip():
#             data_dict = {
#             'Linked': value,
#             }
# # Saving Data into Csv file
# field_names = ['Linked']
# with open('Linked.csv', 'a') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames = field_names)
#     writer.writeheader()
#     writer.writerows(data_dict)
# csvfile.close()      

import csv
csv_file_path = './new_new_data.csv'
column_index = 21
data_list = [] 
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)
    for row in csv_reader:
        value = row[column_index]
        if value.strip():
            data_dict = {
                'Linked': value,
            }
            data_list.append(data_dict)
field_names = ['Linked']
with open('Linked.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    if csvfile.tell() == 0:
        writer.writeheader()
    writer.writerows(data_list)
