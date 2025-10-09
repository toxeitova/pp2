#1
from datetime import date, timedelta
today = date.today()
print("Today's date:", today)
five_days_ago = today - timedelta(days=5)
print("Date five days ago:", five_days_ago)


#2
from datetime import date, timedelta
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#3
from datetime import datetime
now = datetime.now()
print("Before removing microseconds:", now)

no_microseconds = now.replace(microsecond=0)
print("After removing microseconds:", no_microseconds)

#4
from datetime import datetime

date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
difference = abs((date2 - date1).total_seconds())
print(f"Difference between dates in seconds: {difference}")

