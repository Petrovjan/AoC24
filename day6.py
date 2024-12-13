raw = open("day6.txt").read().split("\n")
field = [list(x) for x in raw]
width = len(field[0])
field.append(["0" for y in range(width)])
field.insert(0, ["0" for z in range(width)])
for k in range(len(field)):
    field[k].append("0")
    field[k].insert(0, "0")

#0-UP; 1-RIGHT, 2-DOWN, 3-LEFT

def findStart(input):
    for m in range(len(input)):
        for n in range(len(input[m])):
            if input[m][n] == "^":
                return (m,n)

def walk(field):
    visited = dict()
    curDir = 0
    dirs = [[-1,0],[0,1],[1,0],[0,-1]]
    curR, curC = findStart(field)
    visited[(curR, curC)] = 0

    while True:
        nextR = curR + dirs[curDir][0]
        nextC = curC + dirs[curDir][1]
        if field[nextR][nextC] == "0":
            break
        elif field[nextR][nextC] == "." or field[nextR][nextC] == "^":
            if (nextR, nextC) in visited.keys() and visited[(nextR, nextC)] == curDir:
                return None
            visited[(nextR, nextC)] = curDir
            curR = nextR
            curC = nextC
        elif field[nextR][nextC] == "#":
            curDir = (curDir + 1)%4
        else:
            print("ERROR")

    return len(visited)

print(walk(field))

tempField = []
partTwo = 0
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == ".":
            field[i][j] = "#"
            if not walk(field):
                partTwo += 1
            field[i][j] = "."
print(partTwo)