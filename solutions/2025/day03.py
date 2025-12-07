def max_joltage(bank, num_batteries):
    joltage = 0
    
    start_idx = 0
    final_idx = len(bank) - num_batteries
    for _ in range(num_batteries):
        max_idx = start_idx
        for idx in range(start_idx, final_idx + 1):
            if bank[idx] > bank[max_idx]:
                max_idx = idx
        joltage = 10 * joltage + bank[max_idx]
        
        start_idx = max_idx + 1
        final_idx += 1
    return joltage        

def main(data):
    count1 = count2 = 0
    for bank in data.split("\n"):
        bank = [int(x) for x in bank]
        count1 += max_joltage(bank, 2)
        count2 += max_joltage(bank, 12)
    return count1, count2