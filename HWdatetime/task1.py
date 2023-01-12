# import datetime lib (get ready for more useful comments lmao)
import datetime as dt
import locale
# the languages are set here (i warned you)
# also linux locales moment
LANGS = ["ru_RU.UTF-8", "de_DE.UTF-8", "en_US.UTF-8", "fr_FR.UTF-8"]

date = dt.datetime.fromisocalendar(2023, 1, 1)

maxlen = 0
names = []

for lo in LANGS:
    try:
        locale.setlocale(locale.LC_TIME,lo)
    except:
        print(f"\033[93mWarning: Locale {lo} is not available\x1b[0m")
        continue

    names.append([])

    for i in range(7):
        names[-1].append(date.strftime("%A"))
        if len(names[-1][-1]) > maxlen:
            maxlen = len(names[-1][-1])

        date += dt.timedelta(days=1)
    
    date -= dt.timedelta(days=7)

for lang in names:
    print('-'*(7*maxlen+8))
    print('|' + '|'.join([x.rjust(maxlen) for x in lang]) + '|')

print('-'*(7*maxlen+8))
