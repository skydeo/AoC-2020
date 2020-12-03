import timeit
import operator
from functools import reduce

with open("03.in", "r+") as f:
    puzzle_input = [[j for j in i] for i in f.read().splitlines()]

# puzzle_input = [
#     [j for j in i]
#     for i in """..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#""".splitlines()
# ]


def print_map(tree_map, current_pos):
    tree_map = copy.deepcopy(tree_map)
    tree_map[current_pos[1]][current_pos[0]] = "O"
    for row in tree_map:
        print("".join(row))


start_time = timeit.default_timer()


def calculate_arboreal_stops(tree_map, angle):
    dimensions = (len(tree_map[0]), len(tree_map))
    trees_encountered = 0

    pos = (0, 0)
    while True:
        pos = tuple(map(operator.add, pos, angle))
        if pos[1] >= dimensions[1]:
            break
        else:
            pos = tuple(map(operator.mod, pos, dimensions))
            # print_map(tree_map, pos)
            if puzzle_input[pos[1]][pos[0]] == "#":
                trees_encountered += 1
                # print("Hit tree")
            # print()

    return trees_encountered


t_angle = (3, 1)
print(f"Part 1: {calculate_arboreal_stops(puzzle_input, t_angle)}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.")
print()

start_time = timeit.default_timer()

t_angles = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(
    f"Part 2: {reduce(lambda x, y: x * y, [calculate_arboreal_stops(puzzle_input, t_angle) for t_angle in t_angles])}"
)
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.")
