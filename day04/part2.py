lines = None
with open('day04/input.txt') as f:
    lines = list(map(str.strip, f.readlines()))

sp = []
for i in range(len(lines)):
    line = lines[i]
    line = line[10:]

    w, h = line.split("|")
    winning = w.strip().replace("  ", " ").split(" ")
    hand = h.strip().replace("  ", " ").split(" ")

    s = 0
    for n in hand:
        if n in winning:
            s += 1

    sp.append(s)

def q(n):
    if n >= len(sp): return 0

    a = sp[n]
    res = 1
    for i in range(a):
        res += q(n+i+1)
    return res

sum = 0
for i in range(len(sp)):
    sum += q(i)
print(sum)
