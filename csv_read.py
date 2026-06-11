import csv

with open('sample-1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)