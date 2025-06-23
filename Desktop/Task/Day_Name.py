import datetime

print("Enter Date")
date_input = input().strip().split()
month, day, year = map(int, date_input)

date_obj = datetime.date(year, month, day)
day_name = date_obj.strftime("%A").upper()

print(day_name)
