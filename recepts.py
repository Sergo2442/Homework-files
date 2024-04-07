keys = ['ingridient_name', 'quantity', 'measure', ]

with open('recepts.txt', encoding='utf-8') as text:
  cook_book = {}
  for line in text:
    dish = line.strip()
    ingridients = []
    for i in range(int(text.readline())):
      ingridient = text.readline().split(' | ')
      ingridient_dict = dict(zip(keys, ingridient))
      ingridients.append(ingridient_dict)
    cook_book[dish] = ingridients
    text.readline()

print(cook_book )
