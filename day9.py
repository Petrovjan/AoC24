import copy
data = open("day9.txt").read()

files = dict()
space = dict()
disk = []
for i in range(1, len(data)+1, 2):
    files[int((i-1)/2)] = int(data[i-1])
    if len(data) > i:
        space[int((i-1)/2)] = int(data[i])




# buffer = []
# while len(files) > 0:
#     fval = min(files.keys())
#     frep = files[fval]
#     for j in range(frep):
#         disk.append(fval)
#     files.pop(fval)
#     sval = min(space.keys())
#     srep = space[sval]
#     space.pop(sval)
#     while srep > 0:
#         if len(buffer) == 0 and len(files) > 0:
#             lval = max(files.keys())
#             lrep = files[lval]
#             files.pop(lval)
#             buffer = [lval for x in range(lrep)]
#         elif len(files) == 0:
#             break
#         srep -= 1
#         disk.append(buffer.pop())
# while len(buffer) > 0:
#     disk.append(buffer.pop())



for m in range(max(len(files.keys()), len(space.keys()))):
    if m < len(files.keys()):
        fks = list(files.keys())
        fval = fks[m]
        frep = files[fval]
        disk.append([fval, frep])
    if m < len(space.keys()):
        sks = list(space.keys())
        sval = sks[m]
        srep = space[sval]
        disk.append([None, srep])

newdisk = copy.deepcopy(disk)
for o in range(len(disk)-1, -1, -1):
    a = disk[o]
    if disk[o][0]:
        reppos = newdisk.index(disk[o])
        for s in range(len(newdisk)):
            b = newdisk[s]
            if newdisk[s][0] is None:
                if s > reppos:
                    break
                if newdisk[s][1] >= disk[o][1]:
                    newdisk[s][1] = newdisk[s][1] - disk[o][1]
                    newdisk.remove(disk[o])
                    newdisk.insert(reppos, [None, disk[o][1]])
                    newdisk.insert(s, disk[o])
                    if newdisk[s+1][1] == 0:
                        newdisk.pop(s+1)
                    break


fdisk = []
for x in range(len(newdisk)):
    fv = newdisk[x][0]
    fr = newdisk[x][1]
    for y in range(fr):
        fdisk.append(fv)

solution = 0
for k in range(len(fdisk)):
    if fdisk[k] is not None:
        solution += (k*fdisk[k])
print(solution)

