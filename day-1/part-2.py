dial = 50
count = 0
with open("input.txt") as file:
    for line in file:
        line_strip = line.rstrip()
        direction = line_strip[0]
        change = int(line_strip.replace("L", "").replace("R", ""))
        for _ in range(change):
            if direction == "L":
                dial -= 1
            else:
                dial += 1
            dial = dial % 100
            if dial == 0:
                count += 1
print(count)