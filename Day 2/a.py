lines = []

with open('input.txt') as f:
    rows = f.read().split('\n')

total_score = 0

w = 6
d = 3
l = 0

r = 1
p = 2
s = 3

game_scores = {
    'A X': d + r,
    'A Y': w + p,
    'A Z': l + s,
    'B X': l + r,
    'B Y': d + p,
    'B Z': w + s,
    'C X': w + r,
    'C Y': l + p,
    'C Z': d + s,
}

print(f'Part 1: {sum([game_scores.get(row, 0) for row in rows])}')

game_scores = {
    'A X': l + s,
    'A Y': d + r,
    'A Z': w + p,
    'B X': l + r,
    'B Y': d + p,
    'B Z': w + s,
    'C X': l + p,
    'C Y': d + s,
    'C Z': w + r,
}

print(f'Part 2: {sum([game_scores.get(row, 0) for row in rows])}')
