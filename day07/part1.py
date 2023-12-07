lines = None
with open('day07/input.txt') as f:
    lines = map(str.strip, f.readlines())

# 2 3 4 5 6 7 8 9 T J Q K A
def card_value(c: str):
    return "23456789TJQKA".index(c) + 1

def count_of(a, l):
    n = 0
    for x in l:
        if x == a: n += 1
    return n

# five of kind    55555 -> 25
# four of kind    55551 -> 17
# full house      33322 -> 13
# three of kind   33311 -> 11
# two pair        22221 -> 9
# one pair        22111 -> 7
# high card       11111 -> 5
def primary(h: str) -> int:
    hh = list(h)
    s = 0
    for x in hh:
        s += count_of(x, hh)
    return s

def secondary(h: str) -> int:
    s = 0
    for c in h:
        s = s * 15 + card_value(c)
    return s

def hand_value(h):
    return 1000000 * primary(h) + secondary(h)

arr = []
for line in lines:
    hand, bet = line.split(" ")
    arr.append((hand, int(bet), hand_value(hand)))

arr.sort(key = lambda tuple: tuple[2])

sum = 0
for i in range(len(arr)):
    tuple = arr[i]
    bet = tuple[1]
    sum += (i+1) * bet

print(sum)
