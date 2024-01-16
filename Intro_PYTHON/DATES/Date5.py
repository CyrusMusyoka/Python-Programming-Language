# date difference for something on a certain date
import datetime

nextBirthday = datetime.datetime.strptime('10/10/2023', "%d/%m/%Y").date()
currentDate = datetime.date.today()
#if you subract the two dates you get the difference of days
# between those two dates
difference = nextBirthday - currentDate
print(currentDate.strftime('%A %d %b %Y') )
print(difference.days)
