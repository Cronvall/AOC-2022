lines = []
sections = []
result = 0

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        a = line.split(',')
        sec = a[0].split('-')
        sec[0], sec[1] = int(sec[0]), int(sec[1])
        sections.append(sec)
        sec = a[1].split('-')
        sec[0], sec[1] = int(sec[0]), int(sec[1])
        sections.append(sec)


def contains_other(arr1, arr2):
    larger = []
    smaller = []
    if (arr2[1]-arr2[0]) > (arr1[1]-arr1[0]):
        larger = arr2
        smaller = arr1
    else:
        larger = arr1
        smaller = arr2

    if larger[0] <= smaller[0] and smaller[0] <= larger[1] and smaller[1] <= larger[1]:
        global result
        result = result + 1


for i in range(0, len(sections)):
    if i % 2 == 0:
        contains_other(sections[i], sections[i+1])

print(result)
