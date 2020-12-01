import timeit

with open("01.in", "r+") as f:
    puzzle_input = [int(i) for i in f.read().splitlines()]

l = len(puzzle_input)

for i in range(l):
    for j in range(i + 1, l):
        if puzzle_input[i] + puzzle_input[j] == 2020:
            print("Part 1: " + str(puzzle_input[i] * puzzle_input[j]))
        for k in range(j + 1, l):
            if puzzle_input[i] + puzzle_input[j] + puzzle_input[k] == 2020:
                print(
                    "Part 2: "
                    + str(puzzle_input[i] * puzzle_input[j] * puzzle_input[k])
                )
