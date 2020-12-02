# import timeit

with open("02.in", "r+") as f:
    puzzle_input = [i for i in f.read().splitlines()]

# puzzle_input = """1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc""".splitlines()


def process_input(puzzle_input):
    processed_input = []
    for line in puzzle_input:
        [ranges, char, password] = line.split()
        [min_chars, max_chars] = map(int, ranges.split("-"))
        char = char[:-1]
        processed_input.append([min_chars, max_chars, char, password])

    return processed_input


def validate_passwords(password_list):
    valid_passwords = 0
    for password in password_list:
        [min_chars, max_chars, char, password] = password
        char_count = password.count(char)
        if char_count >= min_chars and char_count <= max_chars:
            valid_passwords += 1

    return valid_passwords


lines = process_input(puzzle_input)
print("Part 1: " + str(validate_passwords(lines)))


def validate_passwords_correctly(password_list):
    valid_passwords = 0
    for password in password_list:
        [pos_1, pos_2, char, password] = password
        if sum([password[pos_1 - 1] == char, password[pos_2 - 1] == char]) == 1:
            valid_passwords += 1

    return valid_passwords


print("Part 2: " + str(validate_passwords_correctly(lines)))
