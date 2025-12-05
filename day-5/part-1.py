fresh = []
ranges = []
count = 0

with open("input.txt") as file:
    for line in file:
        line = line.rstrip()
        if "-" in line:
            num1 = int(line.split("-")[0])
            num2 = int(line.split("-")[1])
            ranges.append((num1, num2))

with open("input.txt") as file:
    for line in file:
        line = line.rstrip()
        if "-" in line:
            pass
        elif line == "":
            pass
        else:
            num = int(line)
            inRange = False
            for x in ranges:
                if x[0] <= num <= x[1]:
                    inRange = True
                    break
            if inRange:
                count += 1

print(count)