raw = open("day2.txt").read().split("\n")
data = []
for i in raw:
    data.append(i.split())

def isSafeDown(report, saved = 0):
    recLen = len(report)
    for j in range(1, recLen):
        if 0 < (int(report[j - 1]) - int(report[j])) < 4:
            continue
        elif saved == 0:
            if isSafeDown(report[:j] + report[j+1:], 1) or isSafeDown(report[:j-1] + report[j:], 1):
                return 1
            else:
                return 0
        else:
            return 0
    return 1

def isSafeUp(report, saved = 0):
    recLen = len(report)
    for k in range(1, recLen):
        if 0 < (int(report[k]) - int(report[k - 1])) < 4:
            continue
        elif saved == 0:
            if isSafeUp(report[:k] + report[k+1:], 1) or isSafeUp(report[:k-1] + report[k:], 1):
                return 1
            else:
                return 0
        else:
            return 0
    return 1

correct = 0

for report in data:
    if report[0] == report[1]:
        if report[1] == report[2]:
            continue
        elif isSafeDown(report[1:], 1) or isSafeUp(report[1:], 1):
            correct += 1
    else:
        if isSafeDown(report) == 1 or isSafeUp(report) == 1:
            correct += 1
        elif (isSafeUp(report[:1] + report[2:], 1) or isSafeDown(report[:1] + report[2:], 1) or
              isSafeUp(report[1:], 1) or isSafeDown(report[1:], 1)):
            correct += 1

print(correct)