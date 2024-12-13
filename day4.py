raw = open("day4.txt").read().split("\n")
data = [list(x) for x in raw]

width = len(data[0])

for i in range(3):
    data.append(["0" for y in range(width)])
    data.insert(0, ["0" for z in range(width)])


for k in range(len(data)):
    for j in range(3):
        data[k].append("0")
        data[k].insert(0, "0")

def findXmas(field, row, col):
    dirs = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
    found = 0
    for dir in dirs:
        word = ""
        for pos in range(4):
            word += field[row + pos*dir[0]][col + pos*dir[1]]
        if word == "XMAS":
            found += 1
    return found

def findMas(field, row, col):
    dirs = [[1,1],[1,-1],[-1,-1],[-1,1]]
    axisOne = False
    if (field[row-1][col-1] == "M" and field[row+1][col+1] == "S") or (field[row-1][col-1] == "S" and field[row+1][col+1] == "M"):
        axisOne = True
    else:
        return 0
    if (field[row-1][col+1] == "M" and field[row+1][col-1] == "S") or (field[row-1][col+1] == "S" and field[row+1][col-1] == "M"):
        return 1
    else:
        return 0

p1 = 0
p2 = 0
for m in range(len(data)):
    for n in range(len(data[m])):
        if data[m][n] == "X":
            p1 += findXmas(data, m, n)
        if data[m][n] == "A":
            p2 += findMas(data, m, n)

print("p1:", p1)
print("p2:", p2)