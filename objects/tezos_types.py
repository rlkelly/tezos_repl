from .basic_types import NoneType, Nat, Int, Tezos
from .tezos import Tezos
from .utils import deep_compare


class Lambda:
    def __init__(self, input_type, return_type, body):
        self.input_type = input_type
        self.return_type = return_type
        self.body = body

    @property
    def type(self):
        return Lambda


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
        self.values = values
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


class Map:
    def __init__(self, key_type, val_type):
        self.key_type = key_type
        self.list_type = key_type
        self.val_type = val_type
        self.value = {}

    def get(self, key):
        assert isinstance(key, self.key_type)
        if key in self.value:
            return Some(self.value[key])
        else:
            return NoneType()

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

    def size(self):
        return len(self.value)

    @property
    def type(self):
        return Map(self.key_type, self.value_type)

    @property
    def key_type(self):
        return self.key_type


class BigMap(Map):
    pass


class Set:
    def __init__(self, set_type):
        self.set_type = set_type
        self.list_type = set_type
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
        return f'Set:{self.set_type}:{self.value}'


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
