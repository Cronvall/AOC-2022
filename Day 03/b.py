
lines = []

with open('input.txt') as f:
    lines = f.readlines()


def group_item(txts) -> int:

    dic = {"lmao"}

    for ch in txts[0]:
        if not ch in dic:
            dic.add(ch)

    for ch in txts[1]:
        if ch in dic:
            for ch in txts[2]:
                if ch in dic:
                    return ord(ch)


total = 0

for i in range(0, len(lines)):
    item = group_item(
        [lines[i],
         lines[min(i+1, len(lines)-1)],
         lines[min(i+2, len(lines)-1)]
         ])
    if item >= 97:
        total = total + (item - 96)
    else:
        total = total + (item - 38)
    i = i + 2


print(total)
