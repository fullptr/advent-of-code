field_checker = {
    "byr": lambda v: in_range(v, 1920, 2002),
    "iyr": lambda v: in_range(v, 2010, 2020),
    "eyr": lambda v: in_range(v, 2020, 2030),
    "hgt": lambda v: (v.endswith("cm") and in_range(v[:-2], 150, 193)) or (v.endswith("in") and in_range(v[:-2], 59, 76)),
    "hcl": lambda v: v.startswith("#") and len(v) == 7 and all(x in "0123456789abcdef" for x in v[1:]),
    "ecl": lambda v: v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda v: len(v) == 9 and v.isdigit(),
    "cid": lambda v: True
}

def in_range(val, min_val, max_val):
    return val.isdigit() and min_val <= int(val) <= max_val

def get_passports(f):
    for line in f.split("\n\n"):
        yield dict(pair.split(":") for pair in line.split())

def part1_validate(passport):
    return {'eyr', 'hgt', 'pid', 'iyr', 'hcl', 'ecl', 'byr'} <= passport.keys()

def part2_validate(passport):
    return all(field_checker[k](v) for k, v in passport.items())

def main(data):
    count_part1 = count_part2 = 0
    for passport in get_passports(data):
        if part1_validate(passport):
            count_part1 += 1
            if part2_validate(passport):
                count_part2 += 1

    return count_part1, count_part2