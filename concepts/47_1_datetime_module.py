import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
print(date)
print(today)

time = datetime.time(10, 30, 45, 100000)
print(time)

now = datetime.datetime.now()
print(now)

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d-%m-%Y %H:%M:%S"))


target_datetime = datetime.datetime(2025, 1, 2, 10, 30, 45, 100000)

current_datetime = datetime.datetime.now()

if target_datetime > current_datetime:
    print("Target datetime is in the future")
else:
    print("Target datetime is in the past")