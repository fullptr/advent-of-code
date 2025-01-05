import parse

def solve(a, b, c, d, e, f):
    det, x, y = a*d-c*b, d*e-c*f, a*f-b*e
    return 3 * x//det + y//det if x % det == y % det == 0 else 0

def main(data):
    count1 = count2 = 0
    pattern = "Button A: X+{:d}, Y+{:d}\nButton B: X+{:d}, Y+{:d}\nPrize: X={:d}, Y={:d}"
    for machine in data.split("\n\n"):
        a, b, c, d, e, f = parse.parse(pattern, machine).fixed
        count1 += solve(a, b, c, d, e, f)
        count2 += solve(a, b, c, d, e + 10**13, f + 10**13)
    return count1, count2