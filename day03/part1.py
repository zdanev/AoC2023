lines = None
with open('day03/input.txt') as f:
    lines = list(map(str.strip, f.readlines()))

def get(x, y):
    try:
        return lines[y][x]
    except:
        return "."
        
def sym(c):
    if c == "." or ("0" <= c and c <= "9"):
        return False
    else:
        return True

def q(x, y):
    return sym(get(x-1, y-1)) or sym(get(x-1, y)) or sym(get(x-1, y+1))  \
        or sym(get(x, y-1)) or sym(get(x, y+1)) \
        or sym(get(x+1, y-1)) or sym(get(x+1, y)) or sym(get(x+1, y+1))

sum = 0
for y in range(len(lines)):
    line = lines[y] + "."
    s = ""
    adj = False
    for x in range(len(line)):
        c = line[x]
        if c.isdigit():
            s += c
            if q(x, y): adj = True
        else:
            if s != "" and adj:
                sum += int(s)
            s = ""
            adj = False

print(sum)
