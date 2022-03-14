import csv

with open("esm_famil_data.csv", 'r', encoding="utf-8") as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        print(line)
