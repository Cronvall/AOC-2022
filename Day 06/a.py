line = ""

with open('input.txt') as f:
    line = f.readline()
print(len(line))
left = 0
right = 3
while right < len(line):
    found = [line[left]]
    if line[left+1] not in found:
        found.append(line[left+1])
    if line[left+2] not in found:
        found.append(line[left+2])
    if line[right] not in found:
        found.append(line[right])
    if len(found) == 4:
        print(found, right)
        break

    left = left + 1
    right = right + 1
