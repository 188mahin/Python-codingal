import calendar
print("list of month names: ")
for monthnum in range(1,13):
    print(f"{monthnum}: {calendar.month_name[monthnum]}")