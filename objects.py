class Unit:
    value = None

class Number(int):
    def neg(self):
        self.value = -self.value
        return self

    def abs(self):
        self.value = abs(self.value)
        return self

    def add(self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value + other.value
        return self

    def mul(self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value * other.value
        return self

    def ediv(self, other):
        assert type(other) in (Nat, Int)
        return Number(self.value // other.value), Number(self.value % other.value)

    def or(self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value | other.value
        return self

    def and (self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value & other.value
        return self

    def xor(self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value ^ other.value
        return self



class Nat(Number):
    def __init__(self, value):
        assert isinstance(value, int)
        assert value >= 0
        self.value = value

    def __repr__(self):
        return f'nat:{self.value}'


class Int(Number):
    def __init__(self, value):
        assert isinstance(value, int)
        self.value = value

    def __repr__(self):
        return f'int:{self.value}'


class Bool:
    def __init__(self, value):
        assert value in ('True', 'False', True, False)
        self.value = value in ('True', True)

    def flip(self):
        self.value = not self.value
        return self

    def __repr__(self):
        return f'bool:{self.value}'


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f'PAIR:(first:{self.first}, second:{self.second})'
