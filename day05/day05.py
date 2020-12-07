import timeit

with open("05.in", "r+") as f:
    puzzle_input = f.read().splitlines()

# puzzle_input = """FBFBBFFRLR
# BFFFBBFRRR
# FFFBBBFRRR
# BBFFBBFRLL""".splitlines()


def find_row(code):
    row_range = list(range(128))
    for c in code:
        if c == "F":
            row_range = row_range[: int(len(row_range) / 2)]
        elif c == "B":
            row_range = row_range[int(len(row_range) / 2) :]
        else:
            print("Invalid symbol.")
            exit()
    return row_range[0]


def find_column(code):
    column_range = list(range(8))
    for c in code:
        if c == "L":
            column_range = column_range[: int(len(column_range) / 2)]
        elif c == "R":
            column_range = column_range[int(len(column_range) / 2) :]
        else:
            print("Invalid symbol.")
            exit()
    return column_range[0]


def find_seat(code):
    row = find_row(code[:7])
    column = find_column(code[7:])

    return row * 8 + column


start_time = timeit.default_timer()
seat_ids = [find_seat(p) for p in puzzle_input]
print(f"Part 1: {max(seat_ids)}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.\n")


def find_missing_seat(seat_ids):
    seat_ids = sorted(seat_ids)
    for seat_id in seat_ids:
        if seat_id + 1 not in seat_ids:
            return seat_id + 1
    return 0


start_time = timeit.default_timer()
print(f"Part 1: {find_missing_seat(seat_ids)}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.\n")
