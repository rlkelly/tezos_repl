from .tezos import Tezos


class Unit(Tezos):
    value = None

    def __repr__(self):
        return 'UNIT'


class Bytes(Tezos):
    pass


class Operation(Tezos):
    def __init__(self):
        pass

    def __str__(self):
        return 'Operation'

    def __repr__(self):
        return 'Operation'


class NoneType(Tezos):
    value = None

    def __init__(self, sometype):
        self.sometype = sometype

    def __repr__(self):
        return 'NONE'


class Number(int):
    def neg(self):
        assert type(other) in (Nat, Int)
        self.value = -self.value
        return Int(self.value)

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

    def bit_and(self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value & other.value
        return self

    def flip(self):
        # bit not
        self.value = ~self.value
        return Int(self.value)

    def lsl(self, other):
        assert isinstance(other, Nat)
        assert other.value <= 256
        self.value = self.value << other.value
        return self

    def lsr(self, other):
        assert isinstance(other, Nat)
        self.value = self.value >> other.value
        return self

    def compare(self, other):
        assert isinstance(other, type(self))
        if self.value == other.value:
            return Int(0)
        if self.value > other.value:
            return Int(1)
        if self.value < other.value:
            return Int(-1)


class Nat(Number, Tezos):
    def __init__(self, value):
        assert isinstance(value, int)
        assert value >= 0
        self.value = value

    def bit_or(self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value | other.value
        return self

    def bit_xor(self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value ^ other.value
        return self

    def add(self, other):
        assert type(other) in (Nat, Int)
        if type(other) == Timestamp:
            return Timestamp(self.value + other.value)
        else:
            if isinstance(other, Nat):
                return Nat(self.value + other.value)
            return Int(self.value + other.value)

    def sub(self, other):
        assert type(other) in (Nat, Int)
        if type(other) == Timestamp:
            return Timestamp(self.value - other.value)
        else:
            return Int(self.value - other.value)

    def mul(self, other):
        assert type(other) in (Nat, Int, Mutez)
        if isinstance(other, Mutez):
            return Mutez(self.value * other.value)
        return Nat(self.value * other.value)

    def ediv(self, other):
        if isinstance(other, Nat):
            return Pair(Nat(self.value // other.value), Nat(self.value % other.value))
        return Pair(Int(self.value // other.value), Nat(self.value % other.value))

    def __repr__(self):
        return f'nat:{int(self.value)}'

    def __str__(self):
        return f'nat:{int(self.value)}'

    @property
    def type(self):
        return Nat


class Timestamp(Nat):
    def add(self, other):
        assert isinstance(other, Int)
        self.value = self.value + other.value
        return self


class Address(Nat):
    pass


class Mutez(Nat):
    def add(self, other):
        assert isinstance(other, Mutez)
        return Mutez(self.value + other.value)

    def sub(self, other):
        assert isinstance(other, Mutez)
        return Mutez(self.value - other.value)

    def mul(self, other):
        assert isinstance(other, Nat)
        return Mutez(self.value * other.value)

    def ediv(self, other):
        assert type(other) in (Mutez, Nat)
        if isinstance(other, Nat):
            return Pair(Mutez(self.value // other.value), Mutez(self.value % other.value))
        return Pair(Nat(self.value // other.value), Nat(self.value % other.value))

    def compare(self, other):
        if self.value < other.value:
            return Int(-1)
        if self.value == other.value:
            return Int(0)
        if self.value > other.value:
            return Int(1)


class Int(Number, Tezos):
    def __init__(self, value):
        assert isinstance(value, int)
        self.value = value

    def __repr__(self):
        return f'int:{int(self.value)}'

    def __str__(self):
        return f'int:{int(self.value)}'

    def add(self, other):
        assert type(other) in (Nat, Int, Timestamp)
        if type(other) == Timestamp:
            return Timestamp(self.value + other.value)
        return Int(self.value + other.value)

    def sub(self, other):
        assert type(other) in (Nat, Int)
        return Int(self.value - other.value)

    def ediv(self, other):
        assert type(other) in (Nat, Int)
        return return Pair(Int(self.value // other.value), Nat(self.value % other.value))

    @property
    def type(self):
        return Int


class Bool(Tezos):
    def __init__(self, value):
        assert value in ('True', 'False', True, False)
        self.value = value in ('True', True)

    def flip(self):
        self.value = not self.value
        return self

    def __repr__(self):
        return f'bool:{self.value}'


class String(Tezos):
    def __init__(self, value):
        assert isinstance(value, str)
        self.value = value

    def concat(self, other):
        assert isinstance(other, String)
        self.value = self.value + other.value
        return self

    def size(self):
        return Nat(len(self.value))

    def compare(self, other):
        if self.value < other.value:
            return Int(-1)
        if self.value == other.value:
            return Int(0)
        if self.value > other.value:
            return Int(1)

    def slice(self, begin, end):
        start = begin.value
        end = end.value
        if start > len(self.value) or end > self.value:
            return NoneType
        return self.value[start:end]

    def __repr__(self):
        return f'string:{self.value}'

    def __str__(self):
        return 'STRING'


if __name__ == '__main__':
    p = Pair(Nat, Nat)
    p((3, 4))

    second = Pair(Nat, Nat)
    third = Pair(Nat, int)

    assert deep_compare(p, second)
    assert not deep_compare(p, third)

    p2 = Pair(Pair(Nat, Nat), Int)
    p2((p, 4))

    second = Pair(Pair(Nat, Nat), Int)
    third = Pair(Nat, int)

    assert deep_compare(p2, second)
    assert not deep_compare(p, third)
