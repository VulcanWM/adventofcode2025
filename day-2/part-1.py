total = 0
with open("input.txt") as file:
    content = file.read()
    for id_range in content.split(","):
        start = int(id_range.split("-")[0])
        end = int(id_range.split("-")[1])
        for id in range(start, end+1):
            if len(str(id)) % 2 == 0:
                first = str(id)[:len(str(id))//2]
                second = str(id)[len(str(id))//2:]
                if first == second:
                    total += id

print(total)