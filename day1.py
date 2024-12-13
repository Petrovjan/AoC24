raw = open("day1.txt").read().split("\n")
firstnums = []
secnums = []
for line in raw:
    a = line.split()
    firstnums.append(int(a[0]))
    secnums.append(int(a[-1]))

firstnums.sort()
secnums.sort()

diff = 0

for i in range(len(firstnums)):
    diff += abs(firstnums[i] - secnums[i])

print(diff)

res = 0
for i in firstnums:
    cis = secnums.count(i)
    res += i * cis

print(res)
res = 0
# for i in range(len(firstnums)):
#     fm = min(firstnums)
#     sm = min(secnums)
#     res += abs(fm - sm)
#     firstnums.remove(fm)
#     secnums.remove(sm)
#
# print(res)

