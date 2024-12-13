raw = open("day5.txt").read().split("\n\n")

rules = [x.split("|") for x in raw[0].split("\n")]
inputs = [y.split(",") for y in raw[1].split("\n")]

myDict = dict()
matched = []
unmatched = []
broken = dict()
bad = False
for i in range(len(inputs)):
    myDict.clear()
    for j in range(len(inputs[i])):
        myDict[inputs[i][j]] = j
    bad = False
    for rule in rules:
        if rule[0] in myDict.keys() and rule[1] in myDict.keys():
            if myDict[rule[0]] > myDict[rule[1]]:
                if i in broken.keys():
                    v = broken[i]
                    v.append(rule)
                    broken[i] = v
                else:
                    broken[i] = [rule]
                bad = True
    if not bad:
        matched.append(i)
    else:
        unmatched.append(i)

res = 0
for l in matched:
    mid = int(len(inputs[l]) / 2)
    res += int(inputs[l][mid])

print(res)

def brokenRules(book, rules):
    brDict = dict()
    br = []
    for m in range(len(book)):
        brDict[book[m]] = m
    bad = False
    for rule in rules:
        if rule[0] in brDict.keys() and rule[1] in brDict.keys():
            if brDict[rule[0]] > brDict[rule[1]]:
                br.append(rule)
                bad = True
    if not bad:
        return None
    else:
        return br


fixed = []
for n in unmatched:
    book = inputs[n]
    brkList = broken[n]
    while brokenRules(book, rules):
        brkList = brokenRules(book, rules)
        for bRule in brkList:
            y = bRule[1]
            book.remove(y)
            book.insert(book.index(bRule[0])+1, y)
    fixed.append(book)

sres = 0
for line in fixed:
    smid = int(len(line)/2)
    sres += int(line[smid])
print(sres)