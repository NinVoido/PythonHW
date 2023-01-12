def gen_row (prow):
    nrow = [1]
    # iterator method zip merges two iterators into one
    for a, b in zip(prow, prow[1:]):
        nrow.append(a+b)
    nrow.append(1)
    return nrow

pas = [[1]]

for i in range(int(input())):
    pas.append(gen_row(pas[i]))

a = len (' '.join([str(char) for char in pas[-1]]))
for i in pas:
    print(' '.join([str(char) for char in i]).center(a))
