lines = None
with open('day02/input.txt') as f:
    lines = map(str.strip, f.readlines())

s = 0
for line in lines:
    a = line.split(":")
    id = int(a[0].replace("Game ", ""))

    r = g = b = 0

    for set in a[1].strip().split(";"):
        for cubes in set.strip().split(","):
            count_, color = cubes.strip().split(" ")
            count = int(count_)

            if color == "red" and count > r: r = count
            if color == "green" and count > g: g = count
            if color == "blue" and count > b: b = count

    print(id, r, g, b)
    s += r * g * b

print (s)