import time
# epoch : a date and time from which a computer measures system time
# epoch = jan 1 1970 00:00:00
# time() returns the number of seconds since epoch
print("time in timestamp/epoch: ",time.time())
print("reference time: ", time.ctime(0))
print("current time: ", time.ctime(time.time()))
print("current local time: ", time.localtime())
print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
time_object = time.localtime()
print("year: ", time_object.tm_year)
print("UTC: ", time.gmtime())
print(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
time_string = "Mon, 01 Jan 2024 12:30:45"
print(time.strptime(time_string, "%a, %d %b %Y %H:%M:%S"))
print("\n=== DIFFERENCE BETWEEN strftime vs strptime ===")

# strftime = "string format time" - converts time object TO string
# strptime = "string parse time" - converts string TO time object

print("\n--- strftime (format time TO string) ---")
time_obj = time.localtime()
print(f"Time object: {time_obj}")
formatted_string = time.strftime("%Y-%m-%d %H:%M:%S", time_obj)
print(f"Formatted string: {formatted_string}")

print("\n--- strptime (parse string TO time) ---")
time_string = "2024-12-19 15:30:45"
print(f"Time string: {time_string}")
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed time object: {parsed_time}")

print("\n=== SUMMARY ===")
print("strftime: time object → string (format)")
print("strptime: string → time object (parse)")

print("\n=== TIME TUPLE ===")
time_tuple = (2020, 5, 20, 5, 21, 10, 0, 2, 4) # (2020 means year, )
time_string = time.asctime(time_tuple)
print(time_string)
# Breaking down the time tuple:
print("\n=== TIME TUPLE BREAKDOWN ===")
time_tuple = (2020, 5, 20, 5, 21, 10, 0, 2, 4)

print("Time tuple structure (9 elements):")
print("Index | Value | Meaning")
print("------|-------|--------")
print(f"  0   |  {time_tuple[0]}  | Year")
print(f"  1   |   {time_tuple[1]}   | Month (1-12)")
print(f"  2   |  {time_tuple[2]}   | Day of month (1-31)")
print(f"  3   |   {time_tuple[3]}   | Hour (0-23)")
print(f"  4   |  {time_tuple[4]}   | Minute (0-59)")
print(f"  5   |  {time_tuple[5]}   | Second (0-59)")
print(f"  6   |   {time_tuple[6]}   | Day of week (0=Monday, 6=Sunday)")
print(f"  7   |   {time_tuple[7]}   | Day of year (1-366)")
print(f"  8   |   {time_tuple[8]}   | Daylight saving time (-1,0,1)")

print(f"\nSo this represents: May 20, 2020 at 5:21:10 AM")
print(f"asctime() converts this tuple to readable format:")
time_string = time.asctime(time_tuple)
print(f"Result: {time_string}")

print(time.mktime(time_tuple))