import timeit

with open("04.in", "r+") as f:
    puzzle_input = f.read().strip()


def process_input(data):
    fixed_records = []
    records = data.split("\n\n")
    for record in records:
        c_record = {}
        if "\n" in record:
            record = record.replace("\n", " ")
        for kv_pair in record.split(" "):
            [k, v] = kv_pair.split(":")
            c_record[k] = v
        fixed_records.append(c_record)

    return fixed_records


def validate_passports(passports):
    valid_passports = 0

    for passport in passports:
        codes = ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
        keys = passport.keys()
        if all([c in keys for c in codes]):
            valid_passports += 1

    return valid_passports


def actually_validate_passports(passports):
    valid_passports = 0

    def isInt(value):
        try:
            int(value)
        except ValueError:
            return False
        return True

    def isYear(value):
        if isInt(value) and len(value) == 4:
            return True
        return False

    def validate_byr(byr_value):
        if isYear(byr_value):
            byr_value = int(byr_value)
            if 1920 <= byr_value <= 2002:
                return True
        return False

    def validate_iyr(iyr_value):
        if isYear(iyr_value):
            iyr_value = int(iyr_value)
            if 2010 <= iyr_value <= 2020:
                return True
        return False

    def validate_eyr(eyr_value):
        if isYear(eyr_value):
            eyr_value = int(eyr_value)
            if 2020 <= eyr_value <= 2030:
                return True
        return False

    def validate_hgt(hgt_value):
        hgt_num = hgt_value[:-2]
        hgt_unit = hgt_value[-2:]
        if hgt_unit in ["cm", "in"] and isInt(hgt_num):
            hgt_num = int(hgt_num)
            if hgt_unit == "cm":
                if 150 <= hgt_num <= 193:
                    return True
            if hgt_unit == "in":
                if 59 <= hgt_num <= 76:
                    return True
        return False

    def validate_hcl(hcl_value):
        if hcl_value[0] == "#":
            try:
                int(hcl_value[1:], 16)
            except ValueError:
                return False
            return True
        return False

    def validate_ecl(ecl_value):
        if ecl_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
        return False

    def validate_pid(pid_value):
        if isInt(pid_value) and len(pid_value) == 9:
            return True
        return False

    for passport in passports:
        codes = ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
        keys = passport.keys()
        if all([c in keys for c in codes]):
            # if not validate_byr(passport["byr"]):
            #     print(passport["byr"])
            # if not validate_iyr(passport["iyr"]):
            #     print(passport["iyr"])
            # if not validate_eyr(passport["eyr"]):
            #     print(passport["eyr"])
            # if not validate_hgt(passport["hgt"]):
            #     print(passport["hgt"])
            # if not validate_hcl(passport["hcl"]):
            #     print(passport["hcl"])
            # if not validate_ecl(passport["ecl"]):
            #     print(passport["ecl"])
            # if not validate_pid(passport["pid"]):
            #     print(passport["pid"])
            if all(
                [
                    validate_byr(passport["byr"]),
                    validate_iyr(passport["iyr"]),
                    validate_eyr(passport["eyr"]),
                    validate_hgt(passport["hgt"]),
                    validate_hcl(passport["hcl"]),
                    validate_ecl(passport["ecl"]),
                    validate_pid(passport["pid"]),
                ]
            ):
                valid_passports += 1

    return valid_passports


start_time = timeit.default_timer()
passports = process_input(puzzle_input)
print(
    f"Passports processed in {round(timeit.default_timer()-start_time, 4)} seconds.\n"
)

start_time = timeit.default_timer()

print(f"Part 1: {validate_passports(passports)}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.\n")

start_time = timeit.default_timer()
print(f"Part 2: {actually_validate_passports(passports)}")
print(f"Completed in {round(timeit.default_timer()-start_time, 4)} seconds.\n")
