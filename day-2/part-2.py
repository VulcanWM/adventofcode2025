total = 0
with open("input.txt") as file:
    content = file.read()
    print(content)
    for id_range in content.split(","):
        print(id_range)
        start = int(id_range.split("-")[0])
        end = int(id_range.split("-")[1])
        for id in range(start, end+1):
            length = len(str(id))
            str_id = str(id)
            for parts in range(1, 12):
                    if length % parts == 0 and length != parts:
                        parts_arr = []
                        part_length = length//parts
                        for x in range(0, length, parts):
                            parts_arr.append(int(str_id[x:x+parts]))
                        first_el = parts_arr[0]
                        all_same = True
                        for el in parts_arr:
                            if el != first_el:
                                all_same = False
                        if all_same:
                            total += id
                            break

print(total)