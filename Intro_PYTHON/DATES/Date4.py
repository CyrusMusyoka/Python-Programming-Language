#birthday date

import datetime

birthday = input("What is your birthday? ")

birthdate = datetime.datetime.strptime(birthday , "%m/%d/%Y").date()
# datetime.datetime.strptime we used it cos we are calling strftime function which is part of
#datetime class which is in datetime module
print(birthdate)
#print("Your Birthday month is " +birthdate.strptime("%B"))