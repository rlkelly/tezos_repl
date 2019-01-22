class Tezos:
    value = None
    def __hash__(self):
        return hash(self.value)
    def __eq__(self, other):
        return self.value == other.value


class Unit(Tezos):
    value = None

    def __repr__(self):
        return 'UNIT'


class Bytes(Tezos):
    pass


class List(Tezos):
    def __init__(self, list_type):
        self.list_type = list_type
        self.value = []
    def cons(self, value):
        assert isinstance(value, list_type)
        self.value.append(value)
        return self

    def size(self):
        return Nat(len(self.value))


class Or(Tezos):
    def __init__(self, value, other_type, side):
        self.value = value
        if side == 'LEFT':
            self.left, self.right = type(value), other_type
            self.isleft = True
            self.isright = False
        else:
            self.left, self.right = other_type, type(value)
            self.isleft = False
            self.isright = True

    def __repr__(self):
        side = 'LEFT' if self.isleft else 'RIGHT'
        return f'OR::({self.left.__name__}, {self.right.__name__})--{side}::({self.value})'


class NoneType(Tezos):
    value = None

    def __init__(self, sometype):
        self.sometype = sometype

    def __repr__(self):
        return 'NONE'

class Map:
    def __init__(self, key_type, val_type):
        self.key_type = key_type
        self.val_type = val_type
        self.value = {}

    def get(self, key):
        assert isinstance(key, self.key_type)
        return self.value[key]

    def update(self, key, some_value):
        assert isinstance(key, self.key_type)
        if type(some_value) is NoneType:
            self.value[key] = None
            del self.value[key]
        else:
            assert isinstance(some_value.value, self.val_type)
            self.value[key] = some_value.value
        return self

    def contains(self, obj):
        # MEM
        assert isinstance(obj, self.key_type)
        return Bool(obj in self.value)


class BigMap(Map):
    pass


class Set:
    def __init__(self, set_type):
        self.set_type = set_type
        self.value = set()

    def contains(self, obj):
        # MEM
        assert isinstance(obj, self.set_type)
        return Bool(obj in self.value)

    def size(self):
        return Nat(len(self.value))

    def update(self, elt, bool):
        assert isinstance(elt, self.set_type)
        if bool.value == False:
            try:
                self.value.remove(elt)
            except KeyError:
                pass
        elif bool.value == True:
            self.value.add(elt)
        return self

    def __repr__(self):
        return f'Set:{self.set_type.__name__}:{self.value}'


class Some(Tezos):
    def __init__(self):
        self.value = value


class Pair(Tezos):
    def __init__(self, first, second):
        self.left = first
        self.right = second

    def __repr__(self):
        return f'PAIR:(first:{self.left}, second:{self.right})'


class Number(int, Tezos):
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
        return Pair(Number(self.value // other.value), Number(self.value % other.value))

    def bit_and(self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value & other.value
        return self

    def bit_not(self):
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

    def __repr__(self):
        return f'nat:{self.value}'

    def __str__(self):
        return f'nat:{self.value}'


class Int(Number, Tezos):
    def __init__(self, value):
        assert isinstance(value, int)
        self.value = value

    def __repr__(self):
        return f'int:{self.value}'


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
            return None
        return self.value[start:end]

    def __repr__(self):
        return f'string:{self.value}'

    def __str__(self):
        return 'STRING'
