dial = 50
count = 0
with open("input.txt") as file:
    for line in file:
        line_strip = line.rstrip()
        if line_strip.startswith("L"):
            # left
            dial -= int(line_strip.replace("L", ""))
            while dial < 0:
                dial += 100
        else:
            # right
            dial += int(line_strip.replace("R", ""))
            while dial > 99:
                dial -= 100
        if dial == 0:
            count += 1
print(count)