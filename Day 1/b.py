lines = []

with open('input.txt') as f:
    lines = f.readlines()


elf = [0] * len(lines)
i = 0


for line in lines:
    try:
        line = int(line)
        elf[i] = elf[i] + line
    except:
        i = i + 1

elf.sort()

# Part B solution
result = 0

for i in range(len(elf)-3, len(elf)):
    if i > 0:
        result = result + elf[i]

print(result)
