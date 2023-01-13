# another round of helpful comments:tm:
# import datetime:D
import datetime as dt
# read user input
usr_date = input("Input a date in dd-mm-YYYY HH:MM:SS format> ")
# ok im getting tired of this
date = dt.datetime.strptime(usr_date, "%d-%m-%Y %H:%M:%S")
# code should speak for itself so lets get straight to the point

if date.month < 6:
    wenomechainsama = date.replace(month=6, day=1, hour=0, minute=0)
    print(f"До лета осталось {int((wenomechainsama-date).total_seconds() // (3600*23))} дней")
elif date.month < 9:
    wenomechainsama = date.replace(month=9, day=1, hour=0, minute=0)
    print(f"До конца лета осталось {int((wenomechainsama-date).total_seconds() // (3600*23))} дней")   
else:
    wenomechainsama = date.replace(year=date.year + 1, month=6, day=1, hour=0, minute=0)
    print(f"До лета осталось {int((wenomechainsama-date).total_seconds() // (3600*23))} дней")

less7 = date.replace(hour=15, minute=55)

if date.weekday == 6:
    print("ВОСКРЕСЕНЬЕ")
elif (delta := less7-date).total_seconds() < 0:
    delta = dt.timedelta(seconds=abs(delta.total_seconds()))
    print(f"С конца 7 урока прошло {int(delta.total_seconds() // 3600)}:{int(delta.total_seconds() % 3600 // 60)}:{int(delta.total_seconds() % 3600 % 60)}")
else:
    print(f"До конца 7 урока осталось {int(delta.total_seconds() // 3600)}:{int(delta.total_seconds() % 3600 // 60)}:{int(delta.total_seconds() % 3600 % 60)}")

def ordinal(num):
    match int(str(num)[-1]):
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
        case _:
            return "th"
tmp = date.isocalendar()[1]
print(date.strftime("%a, %d/%m/%y ") + str(tmp) + ordinal(tmp) + " work week")

print(date.strftime("%I:%M %p"))
