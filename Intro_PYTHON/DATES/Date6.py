import datetime

userInput = input("Enter your birthday date (day-month-year): \n")

birthDay = datetime.datetime.strptime(userInput,'%d-%m-%Y').date()

print(birthDay)

currentDate = datetime.date.today()
print(currentDate)

DateDiff = currentDate - birthDay
print(DateDiff.days)

