def main(data):
    elves = data.split("\n\n")
    elf_sums = (sum(int(x) for x in elf.split("\n") if x) for elf in elves)
    first, second, third, *_ = sorted(elf_sums, reverse=True)
    return first, first + second + third