import datetime

UserInput = input("Enter date of birthday: ")
birthday = datetime.datetime.strptime(UserInput, '%d-%m-%Y').date()
print(birthday)

currentDate = datetime.date.today()
print(currentDate)

ageDiff = currentDate - birthday
print(ageDiff.days)
