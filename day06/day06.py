import timeit

with open("06.in", "r+") as f:
    puzzle_input = f.read()

# puzzle_input = """abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b"""


def process_input(puzzle_input):
    declarations = [p.split("\n") for p in puzzle_input.split("\n\n")]
    return declarations


def count_yeses(declarations):
    yeses = []
    for declaration in declarations:
        yeses.append(len(set(list("".join(declaration)))))
    return yeses


start_time = timeit.default_timer()
declarations = process_input(puzzle_input)
yeses = count_yeses(declarations)
print(f"Part 1: {sum(yeses)}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.\n")
