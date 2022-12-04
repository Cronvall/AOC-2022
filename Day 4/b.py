def a_to_b(bounds): return set([i for i in range(bounds[0], bounds[1] + 1)])
def ints(list_of_numbers): return [int(n) for n in list_of_numbers]
def shared_sections(pair): return pair[0].intersection(pair[1])
def contains(pair): return shared_sections(pair) in pair
def overlaps(pair): return not not shared_sections(pair)
def countif(list, func): return len([pair for pair in list if func(pair)])


data = open('input.txt', 'r').read().strip().split()
data = [[a_to_b(ints(section.split('-')))
        for section in pair.split(',')]
        for pair in data]

print(f'Part 1: {countif(data, contains)}')
print(f'Part 2: {countif(data, overlaps)}')
