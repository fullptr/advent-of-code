def next_state(state):
    new_state = state[1:] + state[:1]
    new_state[6] += new_state[-1]
    return new_state

def main(data):
    state = [0] * 9
    for n in [int(n) for n in data.split(",")]:
        state[n] += 1
        
    for _ in range(80):
        state = next_state(state)
    part1 = sum(state)

    for _ in range(256 - 80):
        state = next_state(state)
    part2 = sum(state)
    
    return part1, part2