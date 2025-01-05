from collections import defaultdict

def process_rules(lines):
    for line in lines:
        container, bags = line.split(" bags contain ")
        bags = bags.replace(" bags", "").replace(" bag", "").replace(".", "").replace("\n", "")
        if "no other" == bags:
            yield container, []
        else:
            yield container, [(int(bag[0]), bag[2:]) for bag in bags.split(", ")]

def part1(lines):
    containers = defaultdict(set)
    for container, bags in process_rules(lines):
        for amount, bag in bags:
            containers[bag].add(container)

    output = set(containers["shiny gold"])
    to_process = set(containers["shiny gold"])

    while len(to_process) > 0:
        x = to_process.pop()
        output |= containers[x]
        to_process |= containers[x]

    return len(output)

def number_of_children(data, curr):
    return sum(amount * (1 + number_of_children(data, bag)) for amount, bag in data[curr])

def part2(lines):
    data = {container: bags for container, bags in process_rules(lines)}
    return number_of_children(data, "shiny gold")

with open("day07_input.txt") as f:
    lines = list(f.readlines())

print(part1(lines))
print(part2(lines))
