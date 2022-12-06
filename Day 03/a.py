lines = []

with open('input.txt') as f:
    lines = f.readlines()


def find_dup(txt) -> int:
    l = len(txt)
    comp1 = txt[:l//2]
    comp2 = txt[l//2:]

    dic = {"lmao"}

    for ch in comp1:
        if not ch in dic:
            dic.add(ch)

    for ch in comp2:
        if ch in dic:
            return ord(ch)


# print(ord(find_dup("vJrwpWtwJgWrhcsFMMfFFhFp")))

total = 0

for line in lines:
    line_val = find_dup(line)
    if line_val >= 97:
        total = total + (line_val - 96)
    else:
        total = total + (line_val - 38)


print(total)
