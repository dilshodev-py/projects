import csv

# with open('employee_file.csv', mode='w') as employee_file:
#
#     employee_writer = csv.writer(employee_file, delimiter=',')
#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

with open('employee_file2.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = '|')
    for i in csv_reader:
        print(i)


# d = [
#     {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'},
#     {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'},
#     {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'},
#     {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'},
#     {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'},
#     {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'},
#     {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'},
#     {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'},
#     {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'}
# ]

# with open('employee_file2.csv', mode='w') as csv_file:
#     fieldnames = ['emp_name', 'dept', 'birth_month']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='|')
#     writer.writeheader()
#     for i in d:
#         writer.writerow(i)
