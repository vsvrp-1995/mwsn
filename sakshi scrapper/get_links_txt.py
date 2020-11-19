import csv
filename = '2020_01.csv' #csv file
output = '2020_01_links.txt' #txt file
links = []
with open(filename, 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[0] != "వీడియోలు" and row[0] != "ఫొటోలు":
            print(row[2])
            links.append(row[2])

with open(output, 'w') as output:
    for row in links:
        output.write(str(row) + '\n')