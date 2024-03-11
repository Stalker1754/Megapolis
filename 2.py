import csv

with open("products.csv", encoding="utf-8") as file:
    reader = list(csv.DictReader(file, delimiter = ';'))
    for i in reader:
        

with open("products_new.csv", "w", encoding="utf-8", newline="") as new_file:
    writer = csv.writer(new_file)
    writer.writerow("Category", "product", "Date", "Price per unit", "Count", "total")