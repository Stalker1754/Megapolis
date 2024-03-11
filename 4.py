import csv

with open("products.csv", encoding="utf-8") as file:
    reader = list(csv.DictReader(file, delimiter = ';')) #Открываем файл

    for i in range(len(reader)):
        pro = reader[i]["product"].split() #Создаем переменную для названия
        duct = reader[i]["Date"].split(".") #Создаем переменную для даты
        promo = (pro[0][2:]+duct[0]+pro[-1][-1]+pro[-1][-2]+duct[1][-2]+duct[1][-1])
        reader[i] = {"Category": reader[i]["Category"], "product": reader[i]["product"], "Date": reader[i]["Date"],
                     "Price per unit": reader[i]["Price per unit"], "Count": reader[i]["Count"], "promocode": promo} #Записываем промокод

with open("product_promo.csv", "w", encoding="utf-8", newline="") as new_file:
    writer = csv.DictWriter(new_file, fieldnames=["Category", "product", "Date", "Price per unit", "Count", "promocode"],delimiter = ";") #Создаем новый файл
    writer.writeheader()
    writer.writerows(reader)