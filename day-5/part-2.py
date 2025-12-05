ranges = []

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if "-" in line:
            a, b = map(int, line.split("-"))
            lo, hi = min(a, b), max(a, b)
            ranges.append((lo, hi))

ranges.sort(key=lambda x: x[0])

merged = []
cur_lo, cur_hi = ranges[0]

for lo, hi in ranges[1:]:
    if lo <= cur_hi + 1:  # overlap or touching
        cur_hi = max(cur_hi, hi)
    else:
        merged.append((cur_lo, cur_hi))
        cur_lo, cur_hi = lo, hi

merged.append((cur_lo, cur_hi))

# count total ids
total = sum(hi - lo + 1 for lo, hi in merged)

print(total)
