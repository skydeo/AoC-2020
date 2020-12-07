import timeit

with open("06.in", "r+") as f:
    puzzle_input = f.read().strip()

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


# def correctly_count_yeses(declarations):
#     yeses = []
#     for declaration in declarations:
#         group_size = len(declaration)
#         all_declared = 0
#         joined_answers = "".join(declaration)
#         print(f"joined_answers: {joined_answers}")
#         for char in set(list(joined_answers)):
#             print(f"char: {char}")
#             print(f"count: {joined_answers.count(char)}")
#             if joined_answers.count(char) == group_size:
#                 all_declared += 1
#                 print("yes")
#         yeses.append(all_declared)
#         print()
#     return yeses


def correctly_count_yeses(declarations):
    yeses = []
    for declaration in declarations:
        chars = set(list("".join(declaration)))
        unanimous_yeses = sum(
            [
                all([char in passenger for passenger in declaration])
                for char in sorted(chars)
            ]
        )
        yeses.append(unanimous_yeses)
    return yeses


start_time = timeit.default_timer()
yeses = correctly_count_yeses(declarations)
print(f"Part 2: {sum(yeses)}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.\n")
