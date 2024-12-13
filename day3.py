import re

input = open("day3.txt").read()
print(input)
#input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
results = []
start = 0
found = 0
enabled = True
while found >= 0:
    found = input.find("mul(")
    if found < 0:
        break

#comment this block to get p1 result
    slice = input[:found]
    instr = re.findall("do\(\)|don't\(\)", slice)
    if len(instr) > 0 and instr[-1] == "don't()":
        enabled = False
    elif len(instr) > 0 and instr[-1] == "do()":
        enabled = True

    input = input[found:]
    end = input.find(")")
    if end < 0:
        input = input[1:]
        break
    candidate = input[:end+1]
    if re.search("^mul\(\d+,+\d+\)$", candidate) and enabled:
        results.append(re.findall("\d+", candidate))
    input = input[1:]


print(results)
res = 0
for seq in results:
        res += int(seq[0])*int(seq[1])
print(res)