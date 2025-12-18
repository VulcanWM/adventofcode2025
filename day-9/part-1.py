coordinates = []
highest_area = 0

with open("input.txt") as file:
    for line in file:
        line = line.rstrip()
        coordinates.append(line)

for i in coordinates:
    for j in coordinates:
        x1 = int(i.split(",")[0])
        y1 = int(i.split(",")[1])
        x2 = int(j.split(",")[0])
        y2 = int(j.split(",")[1])
        area = abs(x1-x2+1) * abs(y1-y2+1)
        if area > highest_area:
            highest_area = area

print(highest_area)