total = 0
with open("input.txt") as file:
    for line in file:
        highest = 0
        for i in range(0, len(line)-11):
            for j in range(i+1, len(line)-10):
                num = int(str(line[i]) + str(line[j]))
                if num > highest:
                    highest = num
        total += highest

print(total)