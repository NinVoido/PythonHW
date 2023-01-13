import names
from random import randint

a = open("test_lvl1alt1.txt", "w")

amo = int(input("Lines to generate: "))
for i in range(amo):
    # write random name
    a.write(names.get_last_name() + " " + 
            names.get_first_name()[0] + "." + 
            names.get_first_name(gender="male")[0] + ".;")
    
    (mob, offs) = (randint(1, 12), randint(1, 2))
    (dab, dae) = sorted([randint(1, 28), randint(1, 28)])
    
    if (12-mob) < offs:
        moe = randint(mob, 12)
    else:
        moe = mob+offs
    a.write(f" {str(dab)}/{str(mob)}; {str(dae)}/{str(moe)}\n")

a.close()
