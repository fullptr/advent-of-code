
def apply_mask_part1(num, mask):
    ret = num
    for idx, bit in enumerate(reversed(mask)):
        if bit == "X":
            continue

        bit_val = 2 ** idx
        if bit == "1" and num & bit_val == 0:
            ret += bit_val
        elif bit == "0" and num & bit_val != 0:
            ret -= bit_val
    return ret

def update(mem, val, addr_masked, index):
    if index == len(addr_masked): # Reached the end
        address = int("".join(addr_masked), 2)
        mem[address] = val

    elif addr_masked[index] in {"0", "1"}:
        update(mem, val, addr_masked, index + 1)

    else:
        addr_masked[index] = "0"
        update(mem, val, addr_masked, index + 1)
        addr_masked[index] = "1"
        update(mem, val, addr_masked, index + 1)
        addr_masked[index] = "X"

def apply_mask_part2(mem, addr, val, mask):
    addr_bits = bin(addr)[2:].zfill(36)
    addr_masked = [m if m != "0" else a for a, m in zip(addr_bits, mask)]
    update(mem, val, addr_masked, 0)

def parse_mem_line(line):
    key, val = line.split(" = ")
    return int(key[4:-1]), int(val)

def part1(lines):
    mem = {}
    mask = "X" * 36
    for line in lines:
        line = line.strip()
        if line.startswith("mem"):
            key, val = parse_mem_line(line)
            mem[key] = apply_mask_part1(val, mask)
        elif line.startswith("mask"):
            mask = line.split(" = ")[1]
    
    return sum(mem.values())

def part2(lines):
    mem = {}
    mask = "X" * 36
    for line in lines:
        line = line.strip()
        if line.startswith("mem"):
            key, val = parse_mem_line(line)
            apply_mask_part2(mem, key, val, mask)
        elif line.startswith("mask"):
            mask = line.split(" = ")[1]

    return sum(mem.values())

with open("day14_input.txt") as f:
    lines = f.readlines()

print(part1(lines))
print(part2(lines))