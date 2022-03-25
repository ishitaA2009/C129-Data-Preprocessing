import csv

data = []

with open("data2.csv","r") as m:
    csvreader = csv.reader(m)
    for row in csvreader:
        data.append(row)

#headers is in 0 index
headers = data[0]
#1: to get all data
planet_data = data[1:]

for data_point in planet_data:
    data_point[0] = data_point[0].lower()

#creating anonymous funtion to sort alphabetically
planet_data.sort(key = lambda planet_data: planet_data[0])

#a+ = appending and writing
with open("data2_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

