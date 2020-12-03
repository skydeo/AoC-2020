import timeit
import operator
import copy

with open("03.in", "r+") as f:
    puzzle_input = [[j for j in i] for i in f.read().splitlines()]

puzzle_input = [
    [j for j in i]
    for i in """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()
]


def print_map(tree_map, current_pos):
    tree_map = copy.deepcopy(tree_map)
    tree_map[current_pos[1]][current_pos[0]] = "O"
    for row in tree_map:
        print("".join(row))


start_time = timeit.default_timer()


def advance_pos(initial_pos, slope, dimensions):
    new_pos = tuple(map(operator.add, initial_pos, slope))
    return tuple(map(operator.mod, new_pos, dimensions))


def calculate_arboreal_stops(tree_map, angle):
    dimensions = (len(tree_map[0]), len(tree_map))
    trees_encountered = 0

    pos = (0, 0)
    while True:
        pos = advance_pos(pos, angle, dimensions)
        print_map(tree_map, pos)
        if puzzle_input[pos[1]][pos[0]] == "#":
            trees_encountered += 1
            print("Hit tree")
        if pos[1] == 0:
            break
        print()

    return trees_encountered


# t_angle = (3, 1)
# print(f"Part 1: {calculate_arboreal_stops(puzzle_input, t_angle)}")
# print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.")


start_time = timeit.default_timer()

# t_angles = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
t_angles = [(1, 2)]

for t_angle in t_angles:
    print(
        f"angle: {t_angle} hit {calculate_arboreal_stops(puzzle_input, t_angle)} trees"
    )
