import solve_funcs


def trows(n):
    return [(i, funcs.apply(i)) for i in [[int(j) for j in format(i, "0" + str(n) + "b")] for i in range(2 ** n)]]


def nullspace(n):
    for i in trows(n):
        if i[1] == [0] * n and i[0] != [0] * n:
            return i[0]
    return None


for i in range(3, 15):
    print(i, nullspace(i))
