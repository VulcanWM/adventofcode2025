# x and then y sliding window
lines = []
with open("input.txt") as file:
    for line in file:
        lines.append(list(line.rstrip()))

totalCount = 0
thisRoundCount = 0
start = True
while thisRoundCount != 0 or start == True:
    thisRoundCount = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            roll = lines[i][j]
            if roll == "@":
                adjacentRolls = 0
                if 0 <= i - 1 < len(lines):
                    if lines[i-1][j] == "@":
                        adjacentRolls += 1
                if 0 <= i + 1 < len(lines):
                    if lines[i+1][j] == "@":
                        adjacentRolls += 1
                if 0 <= j - 1 < len(lines[0]):
                    if lines[i][j-1] == "@":
                        adjacentRolls += 1
                if 0 <= j + 1 < len(lines[0]):
                    if lines[i][j+1] == "@":
                        adjacentRolls += 1
                if 0 <= j - 1 < len(lines[0]) and 0 <= i - 1 < len(lines):
                    if lines[i-1][j-1] == "@":
                        adjacentRolls += 1
                if 0 <= j + 1 < len(lines[0]) and 0 <= i - 1 < len(lines):
                    if lines[i-1][j+1] == "@":
                        adjacentRolls += 1
                if 0 <= j - 1 < len(lines[0]) and 0 <= i + 1 < len(lines):
                    if lines[i+1][j-1] == "@":
                        adjacentRolls += 1
                if 0 <= j + 1 < len(lines[0]) and 0 <= i + 1 < len(lines):
                    if lines[i+1][j+1] == "@":
                        adjacentRolls += 1
                if adjacentRolls < 4:
                    totalCount += 1
                    thisRoundCount += 1
                    lines[i][j] = "."
                start = False

print(totalCount)