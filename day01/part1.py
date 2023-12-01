lines = None
with open('day01/input.txt') as f:
    lines = map(str.strip, f.readlines())

s = 0
for line in lines:
    q = list(filter(str.isdigit, list(line)))
    s += int(q[0] + q[-1])

print(s)
