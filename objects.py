def deep_compare(first, second):
    try:
        if type(first) == Pair:
            assert deep_compare(first.left, second.left_type)
            assert deep_compare(first.right, second.right_type)
            return True
        if type(first) == Or:
            assert type(first.left) == second.left
            assert type(first.right) == second.right
            assert first.isleft == second.isleft
            assert deep_compare(first.value, second.value)
            return True
        if type(first) != second:
            return False
    except AssertionError:
        return False
    return True


class Tezos:
    value = None
    def __hash__(self):
        return hash(self.value)
    def __eq__(self, other):
        return self.value == other.value


class Lambda:
    def __init__(self, input_type, return_type, body):
        self.input_type = input_type
        self.return_type = return_type
        self.body = body

    @property
    def type(self):
        return Lambda


class Unit(Tezos):
    value = None

    def __repr__(self):
        return 'UNIT'

    @property
    def type(self):
        return Unit


class Bytes(Tezos):
    @property
    def type(self):
        return Bytes


class Operation(Tezos):
    def __init__(self):
        pass

    @property
    def type(self):
        return Operation

    def __str__(self):
        return 'Operation'

    def __repr__(self):
        return 'Operation'

class List(Tezos):
    def __init__(self, list_type):
        self.list_type = list_type
        self.value = []

    @classmethod
    def make_new(self, type, values):
        l = List(type)
        l.value = values
        return l

    @property
    def type(self):
        return self

    def __call__(self, values):
        return self

    def cons(self, value):
        assert isinstance(value, self.list_type)
        self.value.append(value)
        return self

    def size(self):
        return Nat(len(self.value))

    def __repr__(self):
        return f'LIST:({self.list_type}, {self.value})'


class Or(Tezos):
    def __init__(self, left_type, right_type):
        self.left_type = left_type
        self.right_type = right_type
    def add_value(self, value, side):
        self.value = value
        if side == 'LEFT':
            assert type(value) == self.left_type
            self.isleft = True
            self.isright = False
        else:
            assert type(value) == self.right_type
            self.isleft = False
            self.isright = True

    @property
    def type(self):
        return Or(self.left_type, self.right_type)

    def __repr__(self):
        side = 'LEFT' if self.isleft else 'RIGHT'
        return f'OR::({self.left.__name__}, {self.right.__name__})--{side}::({self.value})'


class NoneType(Tezos):
    value = None

    def __init__(self, sometype):
        self.sometype = sometype

    @property
    def type(self):
        return self

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

    @property
    def type(self):
        return Map(self.key_type, self.value_type)


class BigMap(Map):
    pass


class Set:
    def __init__(self, set_type):
        self.set_type = set_type
        self.value = set()

    @property
    def type(self):
        return Set(self.set_type)

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
    def __init__(self, value):
        self.value = value

    @property
    def type(self):
        return self


class Pair:
    def __init__(self, first, second):
        self.left_type = first
        self.right_type = second
        self.left = None
        self.right = None

    @property
    def type(self):
        return Pair(self.left_type, self.right_type)

    def __call__(self, values):
        self.left = self.left_type(values[0])
        self.right = self.right_type(values[1])
        return self

    def __getitem__(self, ix):
        if ix == 0:
            return self.left
        return self.right

    def __repr__(self):
        return f'PAIR:(left:{self.left}, right:{self.right})'


class Number(int, Tezos):
    @property
    def type(self):
        return Number

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

    @property
    def type(self):
        return Nat

    def bit_or(self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value | other.value
        return self

    def bit_xor(self, other):
        assert type(other) in (Nat, Int)
        self.value = self.value ^ other.value
        return self

    def __repr__(self):
        return f'nat:{int(self.value)}'

    def __str__(self):
        return f'nat:{int(self.value)}'


class Int(Number, Tezos):
    def __init__(self, value):
        assert isinstance(value, int)
        self.value = value

    @property
    def type(self):
        return Int

    def __repr__(self):
        return f'int:{int(self.value)}'

    def __str__(self):
        return f'int:{int(self.value)}'


class Bool(Tezos):
    def __init__(self, value):
        assert value in ('True', 'False', True, False)
        self.value = value in ('True', True)

    @property
    def type(self):
        return Bool

    def flip(self):
        self.value = not self.value
        return self

    def __repr__(self):
        return f'bool:{self.value}'


class String(Tezos):
    def __init__(self, value):
        assert isinstance(value, str)
        self.value = value

    @property
    def type(self):
        return String

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
