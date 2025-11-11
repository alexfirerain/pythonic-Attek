from random import randint
print(randint(1, 100))


import random
print(random.randint(1, 100))

spisok = ["сок", "вода", "чача"]
for _ in range(5):
    print(random.choice(spisok))

random.shuffle(spisok)  # перемешивает элементы списка
print(spisok)


import datetime

today = datetime.date.today()
print(today)
now = datetime.datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.weekday())
print(now.day)
print(now.year)
print(now.month)
print(now.day)

date = datetime.date(2025, 1, 3)
print(date)
print(date.isoweekday())
print(date.day)
print(date.year)
print(date.month)

time = datetime.time(12, 34, 56)
print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)


now = datetime.datetime.now()
print(now.strftime("%A"))
