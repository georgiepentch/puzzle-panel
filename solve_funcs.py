rows4 = [[int(j) for j in format(i, "04b")] for i in range(2 ** 4)]
rows5 = [[int(j) for j in format(i, "05b")] for i in range(2 ** 5)]
rows6 = [[int(j) for j in format(i, "06b")] for i in range(2 ** 6)]


def apply(t):
    res = [0]*len(t)
    if t[0] == 1:
        res[0] = (res[0] + 1) % 2
        res[1] = (res[1] + 1) % 2
    for i in range(1, len(t) - 1):
        if t[i] == 1:
            res[i - 1] = (res[i - 1] + 1) % 2
            res[i] = (res[i] + 1) % 2
            res[i + 1] = (res[i + 1] + 1) % 2
    if t[len(t) - 1] == 1:
        res[len(t) - 2] = (res[len(t) - 2] + 1) % 2
        res[len(t) - 1] = (res[len(t) - 1] + 1) % 2
    return res


trows4 = [(i, apply(i)) for i in rows4]
trows5 = [(i, apply(i)) for i in rows5]
trows6 = [(i, apply(i)) for i in rows6]


def findt(row):
    dic = []
    if len(row) == 4:
        dic = trows4
    elif len(row) == 5:
        dic = trows5
    elif len(row) == 6:
        dic = trows6

    for i in dic:
        if i[1] == row:
            return i[0]


def transpose(board):
    return [list(i) for i in zip(*board)]


def solve(board):
    sol = [findt(row) for row in board]
    sol = transpose(sol)  # transpose sol
    sol = [findt(row) for row in sol]
    sol = transpose(sol)  # transpose sol again
    if len(board) == 5:
        sol = optimize5(sol)
    return sol


def null5(row):
    row[0] = int(not row[0])
    row[1] = int(not row[1])
    row[3] = int(not row[3])
    row[4] = int(not row[4])


def count1s(row):
    return len([i for i in row if i == 1])


def optimize5(sol):
    changed = False

    for row in sol:
        if count1s(row[:2]) + count1s(row[3:]) >= 2:
            null5(row)
            changed = True

    sol = transpose(sol)

    for row in sol:
        if count1s(row[:2]) + count1s(row[3:]) >= 2:
            null5(row)
            changed = True

    sol = transpose(sol)

    if not changed:
        return sol
    else:
        return optimize5(sol)
