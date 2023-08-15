import csv, time

row_list = []

column = int(input('Which column? '))

start_time = time.time()

with open('event.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        row_list.append(str(row[column]))


largest_field = max(row_list, key=len)
largest_field_size =len(max(row_list, key=len))

finish_time = time.time()

total_time = finish_time - start_time
print(f'Processing took {round(total_time, 2)} seconds to complete.')

print(f'The largest field in column {column} is "{largest_field}" and the size is {largest_field_size} characters long.')
