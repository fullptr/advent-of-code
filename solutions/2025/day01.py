def advance(val, diff, sign):
    wraps = 0
    if sign == "L":
        new_val = val - diff
        while new_val < 0:
            new_val += 100
            wraps += 1
    else:
        new_val = val + diff
        while new_val >= 100:
            new_val -= 100
            wraps += 1
    return new_val, wraps

def main(data):
    val = 50
    count1 = count2 = 0
    
    for line in data.split("\n"):
        d, x = line[0], int(line[1:])
        
        zero_at_start = val == 0
        if d == "L":
            val -= x
            while val < 0:
                val += 100
                count2 += 1
            else:
                if zero_at_start:
                    count2 -= 1
                
        else:
            val += x
            while val >= 100:
                val -= 100
                count2 += 1
            else:
                if val == 0:
                    count2 -= 1
                
        if val == 0:
            count1 += 1
            count2 += 1
            
    return count1, count2