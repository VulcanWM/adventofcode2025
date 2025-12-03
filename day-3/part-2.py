total = 0
with open("input.txt") as file:
    for line in file:
        lastIndex = -1
        num = 0
        digitsPicked = 0
        line = line.rstrip()
        for i in range(12):
            remaining = 12 - digitsPicked
            search_start = lastIndex + 1
            search_end = len(line) - remaining + 1

            slice = line[search_start:search_end]
            thisNum = max(slice)
            index_in_slice = slice.index(thisNum)

            lastIndex = search_start + index_in_slice
            num = num * 10 + int(thisNum)
            digitsPicked += 1
        total += num

print(total)