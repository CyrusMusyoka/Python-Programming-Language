#print current time on real time oclock
import datetime

currentTime = datetime.datetime.now()
print(datetime.datetime.strftime(currentTime,'%H%m %p'))
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

currentDay = datetime.datetime.today()
print(currentDay.date())
print(currentTime.time())