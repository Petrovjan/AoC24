import itertools
raw = open("day7.txt").read().split("\n")
data = [x.split(": ") for x in raw]
dataD = dict()
for line in data:
    if line[0] in dataD.keys():
        print("error")
    dataD[line[0]] = line[1].split(" ")

solution = 0
for res, input in dataD.items():
    opsCount = len(input) - 1
    comb = list(itertools.product("+*|", repeat=opsCount))
    for poss in comb:
        valid = True
        a = int(input[0])
        for o in range(opsCount):
            if poss[o] == "+":
                a += int(input[o+1])
            elif poss[o] == "*":
                a *= int(input[o+1])
            else:
                #valid = False   #uncomment for partOne result
                #break           #uncomment for partOne result
                a = int(str(a)+input[o+1])
        if a == int(res) and valid:
            solution += int(res)
            break

print(solution)