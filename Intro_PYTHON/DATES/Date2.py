import datetime

currentDate = datetime.date.today()

print(currentDate.strftime("%A,%b,%D,%Y"))
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)