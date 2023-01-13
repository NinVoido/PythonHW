import random as r
import randomname

_pool = ["Morgenshtern", "Travis Scott", "Mozart", "Bach", "Slava Marlow", "DJ Khaled",
         "Mr. Beast", "Guchiry", "Inabakumori", "Hatsune Miku"]

r.shuffle(_pool)
_pool = _pool[:r.randint(5, len(_pool)-1)]

a = open("test_lvl23alt1.txt", "w")
amo = int(input("Lines to generate: "))

for i in range(amo):
    a.write(f"{r.choice(_pool)}, {randomname.get_name()}, {r.randint(1990, 2022)}:\n")
    for j in range(r.randint(2, 15)):
        a.write(f"{randomname.get_name()} {r.randint(1, 10)}:{r.randint(0, 59)}\n")
    a.write("---\n")

a.close()
