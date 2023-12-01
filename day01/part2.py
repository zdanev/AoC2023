lines = None
with open('day01/input.txt') as f:
    lines = f.readlines()

s = 0
for line in lines:
    line = line.strip()

    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")

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