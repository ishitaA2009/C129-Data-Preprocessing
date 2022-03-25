import csv

dataset1 = []
dataset2 = []

with open("data.csv","r") as m:
    csvreader = csv.reader(m)
    for row in csvreader:
        dataset1.append(row)

with open("dataset_2_sorted.csv","r") as m:
    csvreader = csv.reader(m)
    for row in csvreader:
        dataset2.append(row)

headers1 = dataset1[0]
planet_data1 = dataset1[1:]

headers2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = headers1+headers2
planet_data = []

for index,data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("final1.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

