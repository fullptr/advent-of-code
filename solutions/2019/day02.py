from dataclasses import dataclass

@dataclass
class Intcode:
    code: list[int]
    ip: int = 0
    
    def step(self):
        op = self.code[self.ip]
        match op:
            case 1:
                lhs, rhs, dst = self.code[self.ip + 1], self.code[self.ip + 2], self.code[self.ip + 3]
                self.code[dst] = self.code[lhs] + self.code[rhs]
                self.ip += 4
            case 2:
                lhs, rhs, dst = self.code[self.ip + 1], self.code[self.ip + 2], self.code[self.ip + 3]
                self.code[dst] = self.code[lhs] * self.code[rhs]
                self.ip += 4
            case _:
                return True
        return False
            
    def run(self):
        while True:
            halt = self.step()
            if halt:
                return self.code[0]
    
def get_code(data):
    return [int(x) for x in data.split(",")]

def do_part2(data):
    for noun in range(0, 100):
        for verb in range(0, 100):
            code = get_code(data)
            code[1] = noun
            code[2] = verb
            output = Intcode(code).run()
            if output == 19690720:
                return 100 * noun + verb
            
def main(data):
    code = get_code(data)
    code[1] = 12
    code[2] = 2
    part1 = Intcode(code).run()
    part2 = do_part2(data)
    
    return part1, part2