import copy

input = "89010123.78121874.87430965.96549874.45678903.32019012.01329801.10456732"

data = input.split(".")
start = []
field = dict()
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "0":
            start.append([i, j])
        field[(i, j)] = int(data[i][j])

dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]

upcoming = []
tops = 0

for pos in start:
    upcoming.append(pos)
    while len(upcoming) > 0:
        newupcoming = copy.deepcopy(upcoming)
        for k in upcoming:
            newupcoming.remove(k)
            for dir in dirs:
                if (k[0] + dir[0], k[1] + dir[1]) in field.keys():
                    if field[(k[0] + dir[0], k[1] + dir[1])] - field[(k[0], k[1])] == 1:
                        if field[(k[0] + dir[0], k[1] + dir[1])] == 9:
                            tops += 1
                            continue
                        newupcoming.append([k[0] + dir[0], k[1] + dir[1]])

        upcoming = copy.deepcopy(newupcoming)
    upcoming.clear()

print(tops)