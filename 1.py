import csv

with open("products.csv", encoding="utf-8") as file:
    reader = list(csv.DictReader(file, delimiter = ';'))
    Zak = 0
    for i in range (len(reader)):
        total = (int(float(reader[i]["Price per unit"]))*int(float(reader[i]['Count'])))
        if reader[i]["Category"]=="Закуски":
            Zak+=total
        reader[i] = {"Category": reader[i]["Category"],"product": reader[i]["product"],"Date": reader[i]["Date"],"Price per unit": reader[i]["Price per unit"],"Count": reader[i]["Count"],"total": total}
print(Zak)

with open("products_new.csv", "w", encoding="utf-8", newline="") as new_file:
    writer = csv.DictWriter(new_file, fieldnames=["Category", "product", "Date", "Price per unit", "Count", "total"],delimiter = ";")
    writer.writeheader()
    writer.writerows(reader)