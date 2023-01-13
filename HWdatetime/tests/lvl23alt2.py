import random as r
import random_names
import randomname

_pool = ["Stanley Kubrik", "Andrey Tarkovsky", "David Lean", "Martin Scorsese", 
         "Alfred Hitchcock", "Tim Burton", "Lars von Trier", "Ridley Scott", 
         "The Coen Brothers", "Christopher Nolan"]

r.shuffle(_pool)
_pool = _pool[:r.randint(5, len(_pool)-1)]

a = open("test_lvl23alt2.txt", "w")

for i in _pool:
    a.write(f"{i}, {random_names.Country()}:\n")
    for j in range(r.randint(2, 15)):
        a.write(f"{randomname.get_name()}, {r.randint(1980, 2022)}, {r.randint(1, 4)}:{r.randint(0, 59)}:{r.randint(0,59)}\n")
    a.write("-----------\n")

a.close()
