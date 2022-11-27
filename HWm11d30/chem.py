def load():
    file = open("./chem.csv", "r")
    # Skip the first line
    _ = file.readline()
    # Iterate through contents
    for line in file:
        info = line.split(",")
        # Remove spaces in the csv
        info[2] = info[2].replace(' ', '')
        
        yield (info[2], info[0], info[3])

elems = {name: (q, m) for (name, q, m) in load()}

for key, elem in elems.items():
    print(f"{key} has a charge of {elem[0]} and a mass of {elem[1]}")
