val = 0
all_seats = set()
with open("day05_input.txt") as f:
    for line in f:
        seat = int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)
        val = max(val, seat)
        all_seats.add(seat)

def find_seat(all_seats):
    for i in range(2**10):
        if i not in all_seats and {i+1, i-1} <= all_seats:
            return i
print(val)
print(find_seat(all_seats))