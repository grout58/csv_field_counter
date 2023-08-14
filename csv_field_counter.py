import csv

row_list = []

column = int(input('Which column? '))

with open('event.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        row_list.append(str(row[column]))


largest_field = max(row_list, key=len)
largest_field_size =len(max(row_list, key=len))

print(f'The largest field in column {column} is "{largest_field}" and the size is {largest_field_size} characters long')
