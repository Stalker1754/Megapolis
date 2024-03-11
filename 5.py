import csv

with open("products.csv", encoding="utf-8") as file:
    reader = list(csv.DictReader(file, delimiter = ';'))
    reader.sort(key=lambda x: x["Count"])
    for i in range(10):
        print(f'{reader[i]["Category"]},{reader[i]["Count"]}')