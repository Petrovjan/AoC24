inpt = "4329 385 0 1444386 600463 19 1 56615"
inpt = inpt.split(" ")
stones = dict()

for inp in inpt:
        stones[inp] = 1

print(stones.items())
newstones = dict()

for i in range(75):
    newstones.clear()
    newstones = stones.copy()
    for key,val in stones.items():
        if val == 0:
                continue
        if key == "0":
            newstones["1"] = newstones.setdefault("1", 0) + val
            newstones[key] = newstones[key] - val
        elif len(key)%2 == 0:
            newstones[key[:int(len(key)/2)]] = newstones.setdefault(key[:int(len(key)/2)], 0) + val
            newstones[str(int(key[int(len(key)/2):]))] = newstones.setdefault(str(int(key[int(len(key)/2):])), 0) + val
            newstones[key] = newstones[key] - val
        else:
            newstones[str(int(key)*2024)] = newstones.setdefault(str(int(key)*2024), 0) + val
            newstones[key] = newstones[key] - val
    stones = newstones.copy()


print(sum(stones.values()))