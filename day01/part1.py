lines = None
with open('day01/input.txt') as f:
    lines = f.readlines()

s = 0
for line in lines:
    line = line.strip()

    a = ""
    b = ""
    for c in line:
        if c.isnumeric(): 
            a = c
            break
    for c in line[::-1]:
        if c.isnumeric(): 
            b = c
            break
    s = s + int(a+b)

print(s)