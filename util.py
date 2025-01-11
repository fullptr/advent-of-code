from dataclasses import dataclass
from itertools import islice

def sliding(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result
    
@dataclass(frozen=True)
class Vec2:
    x: int
    y: int
    
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: int):
        return Vec2(self.x * scalar, self.y * scalar)
    
    def mag2(self):
        return self.x ** 2 + self.y ** 2