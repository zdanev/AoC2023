lines = None
with open('day03/input.txt') as f:
    lines = list(map(str.strip, f.readlines()))

def get(x, y):
    try:
        return lines[y][x]
    except:
        return "."
        
def sym(c):
    return c == "*"

def q(x, y):
    if sym(get(x-1, y-1)): return 1000 * (x-1) + (y-1)
    if sym(get(x-1, y)): return 1000 * (x-1) + (y)
    if sym(get(x-1, y+1)): return 1000 * (x-1) + (y+1)
    if sym(get(x, y-1)): return 1000 * (x) + (y-1)
    if sym(get(x, y+1)): return 1000 * (x) + (y+1)
    if sym(get(x+1, y-1)): return 1000 * (x+1) + (y-1)
    if sym(get(x+1, y)): return 1000 * (x+1) + (y)
    if sym(get(x+1, y+1)): return 1000 * (x+1) + (y+1)
    return None

sum = 0
gears = {}
for y in range(len(lines)):
    line = lines[y] + "."
    s = ""
    gear = None

    for x in range(len(line)):
        c = line[x]
        if c.isdigit():
            s += c
            g = q(x, y)
            if g:
                gear = g
        else:
            if s != "":
                if gear:
                    print(gear, s)
                    
                    prev = gears.get(gear)
                    if prev:
                        sum += int(prev) * int(s)
                    else:
                        gears[gear] = s

            s = ""
            gear = None

print (sum)