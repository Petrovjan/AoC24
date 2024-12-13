import itertools

raw = open("day8.txt").read().split("\n")
field = dict()
antennas = dict()
nodes = dict()
for i in range(len(raw)):
    for j in range(len(raw[i])):
        field[(i, j)] = raw[i][j]
        if raw[i][j] != ".":
            if raw[i][j] in antennas.keys():
                antennas[raw[i][j]].append((i, j))
            else:
                antennas[raw[i][j]] = [(i, j)]

for type, places in antennas.items():
    combinations = itertools.combinations(places, 2)
    for comb in combinations:
        a = comb[0][0] - comb[1][0]
        b = comb[0][1] - comb[1][1]
        c = comb[0][0] + a
        e = comb[1][0] - a
        d = comb[0][1] + b
        f = comb[1][1] - b
        if (c, d) in field.keys():
            nodes[(c, d)] = type
        if (e, f) in field.keys():
            nodes[(e, f)] = type

print(len(nodes))
nodes.clear()

for type, places in antennas.items():
    combinations = itertools.combinations(places, 2)
    for comb in combinations:
        a = comb[0][0] - comb[1][0]
        b = comb[0][1] - comb[1][1]
        failA = False
        failB = False
        for rep in range(len(field)):
            c = comb[0][0] + a*rep
            e = comb[1][0] - a*rep
            d = comb[0][1] + b*rep
            f = comb[1][1] - b*rep
            if (c, d) in field.keys():
                nodes[(c, d)] = type
            else:
                failA = True
            if (e, f) in field.keys():
                nodes[(e, f)] = type
            else:
                failB = True
            if failB and failA:
                break

print(len(nodes))