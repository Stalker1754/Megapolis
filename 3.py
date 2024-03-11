import csv

with open("products.csv", encoding="utf-8") as file:
    reader = list(csv.DictReader(file, delimiter = ';'))
    reader.sort(key=lambda x: x["Count"], reverse=True)
    a = input()
    while a!="молоко":
        for i in reader:
            if a in i["Category"]:
                print(f'В категории: {i["Category"]} товар: {i["product"]} был куплен {i["Count"]} раз')
                break
        else:
            print("Такой категории не существует в нашей БД")
        a = input()

