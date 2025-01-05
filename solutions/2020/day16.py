import math

def contains(val, intervals):
    return any(i[0] <= val <= i[1] for i in intervals)

def parse_interval(string):
    a, b = string.split("-")
    return int(a), int(b)

def parse_input():
    notes = {}
    my_ticket = None
    nearby_tickets = []
    handle_nearby_tickets = False

    with open("day16_input.txt") as f:
        for line in f:
            line = line.strip()
            if handle_nearby_tickets:
                nearby_tickets.append([int(x) for x in line.split(",")])
            elif ": " in line:
                key, vals = line.split(": ")
                notes[key] = {parse_interval(intv) for intv in vals.split(" or ")}
            elif line.startswith("your ticket"):
                my_ticket = [int(x) for x in next(f).split(",")]
            elif line.startswith("nearby tickets"):
                handle_nearby_tickets = True


    return notes, my_ticket, nearby_tickets

def part1(notes, my_ticket, nearby_tickets):
    count = 0
    intervals = set.union(*notes.values())
    for ticket in nearby_tickets:
        count += sum(val for val in ticket if not contains(val, intervals))
    return count

def filter_tickets(nearby_tickets, intervals):
    return [t for t in nearby_tickets if all(contains(val, intervals) for val in t)]

def get_fields(notes, nearby_tickets, ticket_len):
    positions = [set() for _ in range(ticket_len)]
    for pos in range(ticket_len):
        values = {x[pos] for x in nearby_tickets}
        for name, intervals in notes.items():
            if all(contains(x, intervals) for x in values):
                positions[pos].add(name)

    found_fields = {}
    while any(x for x in positions):
        field = None
        for pos, names in enumerate(positions):
            if len(names) == 1:
                field = names.pop()
                if field not in found_fields:
                    found_fields[field] = pos
                    break

        for pos in positions:
            if field in pos:
                pos.remove(field)
    
    return found_fields

def part2(notes, my_ticket, nearby_tickets):
    intervals = set.union(*notes.values())
    nearby_tickets = filter_tickets(nearby_tickets, intervals)
    fields = get_fields(notes, nearby_tickets, len(my_ticket))

    ret = 1
    for field_name, field_index in fields.items():
        if field_name.startswith("departure"):
            ret *= my_ticket[field_index]
    return ret

data = parse_input()
print(part1(*data))
print(part2(*data))
