import csv
# users = [
#     {'emp_name': "John Smith", 'dept': 'Accounting', 'birth_month':'November'},
#     {'emp_name': "Botir", 'dept': 'Accounting', 'birth_month':'November'},
# ]
# with open('employee_file2.csv', mode="a+") as csv_file:
#     fieldnames = ['emp_name', 'dept', 'birth_month']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     csv_file.seek(0)
#     if not list(csv.DictReader(csv_file , delimiter=',')):
#         writer.writeheader()
#     writer.writerows(users)
#
#
# with open('employee_file2.csv') as csv_file:
#     writer = csv.DictReader(csv_file, delimiter = ',')
#     print(list(writer))


# task 1
# import json

# file_path = "/home/dilshod/PycharmProjects/Python_21/module_3/lesson_8/tasks/centers.json"
#
# with open(file_path , mode = "r") as f:
#     data = json.load(f)
#
# with open("center.csv" ,'w' ) as f:
#     fieldnames = list(data[0].keys())
#     writer = csv.DictWriter(f , fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)




