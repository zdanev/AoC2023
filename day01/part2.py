lines = None
with open('day01/input.txt') as f:
    lines = map(str.strip, f.readlines())

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

s = 0
for line in lines:

    for i in range(len(numbers)):
        line = line.replace(numbers[i], numbers[i] + str(i+1) + numbers[i])

    q = list(filter(str.isdigit, list(line)))
    s += int(q[0] + q[-1])

print(s)
