import random_names
from random import randint

a = open("test_lvl1alt2.txt", "w")
amo = int(input("Lines to generate: "))

for i in range(amo):
    viewers = randint(1, 500)
    price = randint(50, 500)
    (d, m, y) = (randint(1, 28), randint(1, 12), randint(2010, 2030))
    a.write(f"{random_names.Places()}, {d}/{m}/{y}, {viewers}, {price}\n")

a.close()
