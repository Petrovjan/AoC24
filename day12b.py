raw = open("day12.txt").read().split("\n")
data = [list(x) for x in raw]
field = dict()
for i in range(len(data)):
    for j in range(len(data[i])):
        field[(i*2,j*2)] = data[i][j]
        field[(i * 2 + 1, j * 2 + 1)] = data[i][j]
        field[(i * 2, j * 2 + 1)] = data[i][j]
        field[(i * 2 + 1, j * 2)] = data[i][j]
# print(field.items())

def getNeigh(field, sp, letter):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    neighbours = []
    for dir in dirs:
        if (sp[0]+dir[0],sp[1]+dir[1]) in field.keys() and field[(sp[0]+dir[0],sp[1]+dir[1])] == letter:
            neighbours.append((sp[0]+dir[0],sp[1]+dir[1]))
    return neighbours

def countCorners(start, plot, border):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]] #R, D, L, U
    curDir = 0
    curR = start[0]
    curC = start[1]
    corners = 1
    while True:
        nextR = curR + dirs[curDir][0]
        nextC = curC + dirs[curDir][1]
        cornerR = curR + dirs[curDir][0] + dirs[curDir - 1][0]
        cornerC = curC + dirs[curDir][1] + dirs[curDir - 1][1]
        if ((curR, curC) == start and curDir == 3):
            if (curR,curC) in border.keys():
                border.pop((curR,curC))
            else:
                print("4", (curR,curC))
            break
        elif ((nextR, nextC) == start and curDir == 3):
            if (nextR, nextC) in border.keys():
                border.pop((nextR, nextC))
            else:
                print("5", (nextR, nextC))
            break
        elif (nextR, nextC) in plot and (cornerR, cornerC) not in plot: #posunout se
            curR = nextR
            curC = nextC
            if (curR,curC) in border.keys():
                border.pop((curR,curC))
            else:
                print("1", (curR,curC))
        elif (cornerR, cornerC) in plot and (nextR, nextC) in plot: #roh, zmena smeru
            corners += 1
            curDir = (curDir - 1) % 4
            curR = nextR
            curC = nextC
            if (curR,curC) in border.keys():
                border.pop((curR,curC))
            else:
                print("2", (curR,curC))
        else: #konec cesty, zmena smeru
            corners += 1
            curDir = (curDir + 1) % 4
            if (curR,curC) in border.keys():
                border.pop((curR,curC))
    return corners, border


def countInside(insideStart, insidePlot, remBorder):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]] #R, D, L, U
    curDir = 2
    curR = insideStart[0]
    curC = insideStart[1]
    corners = 0
    rot = 0
    while True:
        nextR = curR + dirs[curDir][0]
        nextC = curC + dirs[curDir][1]
        cornerR = curR + dirs[curDir][0] + dirs[curDir - 1][0]
        cornerC = curC + dirs[curDir][1] + dirs[curDir - 1][1]
        if ((curR, curC) == insideStart and curDir == 2 and rot >= 3):
            if (curR,curC) in remBorder.keys():
                remBorder.pop((curR, curC))
            else:
                print("I4", (curR,curC))
            break
        elif ((nextR, nextC) == insideStart and curDir == 2):
            if (nextR, nextC) in remBorder.keys():
                remBorder.pop((nextR, nextC))
            else:
                print("I5", (nextR, nextC))
            break
        elif (nextR, nextC) in insidePlot and (cornerR, cornerC) not in insidePlot: #posunout se
            curR = nextR
            curC = nextC
            if (curR,curC) in remBorder.keys():
                remBorder.pop((curR, curC))
            else:
                print("I1", (curR,curC))
        elif (cornerR, cornerC) in insidePlot and (nextR, nextC) in insidePlot: #roh, zmena smeru
            corners += 1
            curDir = (curDir - 1) % 4
            curR = nextR
            curC = nextC
            if (curR,curC) in remBorder.keys():
                remBorder.pop((curR, curC))
            else:
                print("I2", (curR,curC))
        else: #konec cesty, zmena smeru
            rot += 1
            corners += 1
            curDir = (curDir + 1) % 4
            if (curR,curC) in remBorder.keys():
                remBorder.pop((curR, curC))
            else:
                print("I3", (curR,curC))
    return corners, remBorder

result = 0
visitedTotal = dict()
for startPos,letter in field.items():
    if startPos in visitedTotal.keys():
        continue

    fences = 0
    thisArea = dict()
    border = dict()
    nextSteps = [startPos]

    while len(nextSteps) > 0:
        thisStep = nextSteps.pop(0)
        newSteps = getNeigh(field, thisStep, letter)
        for newStep in newSteps:
            if newStep not in thisArea and newStep not in nextSteps:
                nextSteps.append(newStep)
        thisArea[thisStep] = letter
        visitedTotal[thisStep] = letter
        if len(newSteps) < 4:
            border[thisStep] = len(newSteps)

    fences, remBorders = countCorners(startPos, thisArea, border)

    while len(remBorders) > 0:
        minF = 100000
        maxS = 0
        for obl in remBorders.keys():
            if obl[0] < minF:
                minF = obl[0]
        for ob in remBorders.keys():
            if ob[0] == minF:
                if ob[1] > maxS:
                    maxS = ob[1]
        # print((minF,maxS))
        newFences, remBorders = countInside((minF,maxS), thisArea, remBorders)
        fences += newFences
    result += fences*(len(thisArea)//4)

print(result)