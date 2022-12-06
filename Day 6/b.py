line = ""
with open('input.txt') as f:
    line = f.readline()
left = 0
right = 13
while right < len(line):
    found = []
    for i in range(0, 14):
        if line[left+i] not in found:
            found.append(line[left+i])
    if len(found) == 14:
        print(found, right)
        break

    left = left + 1
    right = right + 1
