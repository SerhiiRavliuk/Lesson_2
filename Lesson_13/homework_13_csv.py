import csv

with open('r-m-c.csv', newline='', encoding='utf-8') as first_file:
    reader_1 = csv.reader(first_file)
    for row in reader_1:
        print(', '.join(row))

with open('random-michaels.csv', newline='', encoding='utf-8') as second_file:
    reader_2 = csv.reader(second_file)
    for row in reader_2:
        print(', '.join(row))

input_file = 'random-michaels.csv'
output_file = 'result_Ravliuk.csv'

with open(input_file, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    rows = list(reader)

unique_rows = set()
unique_data = [header]

for row in rows:
    row_tuple = tuple(row)
    if row_tuple not in unique_rows:
        unique_rows.add(row_tuple)
        unique_data.append(row)

with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(unique_data)

print(f'\nОчищений файл збережено як {output_file}')
