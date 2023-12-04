lines = None
with open('day04/input.txt') as f:
    lines = map(str.strip, f.readlines())

sum = 0
for line in lines:
    line = line[10:]

    w, h = line.split("|")
    winning = w.strip().replace("  ", " ").split(" ")
    hand = h.strip().replace("  ", " ").split(" ")

    s = 0
    for n in hand:
        if n in winning:
            if s == 0: s = 1
            else: s *= 2

    sum += s

print(sum)
