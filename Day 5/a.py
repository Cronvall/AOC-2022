
# Create stacks
stacks = [
    ['N', 'W', 'F', 'R', 'Z', 'S', 'M', 'D'],
    ['S', 'G', 'Q', 'P', 'W'],
    ['C', 'J', 'N', 'F', 'Q', 'V', 'R', 'W'],
    ['L', 'D', 'G', 'C', 'P', 'Z', 'F'],
    ['S', 'P', 'T'],
    ['L', 'R', 'W', 'F', 'D', 'H'],
    ['C', 'D', 'N', 'Z'],
    ['Q', 'J', 'S', 'V', 'F', 'R', 'N', 'W'],
    ['V', 'W', 'Z', 'G', 'S', 'M', 'R']
]
for stack in stacks:
    stack.reverse()

# Read stack input
lines = []
with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    row = line.split()
    for i in range(int(row[1])):
        stacks[int(row[5])-1].append(stacks[int(row[3])-1].pop())

result = ""
for stack in stacks:
    result = result + stack.pop()

print(result)
