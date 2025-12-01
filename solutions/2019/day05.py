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