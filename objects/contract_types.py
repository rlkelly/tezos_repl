from .tezos import Tezos
from .basic_types import Unit
from .tezos_types import Or


class Address(Tezos):
    def __init__(self, address):
        assert isinstance(address, str)
        self.address = address
        self.valid_params = []

    def add_type(self, valid_type):
        print(valid_type)
        if isinstance(valid_type, Or):
            self.add_type(valid_type.left_type)
            self.add_type(valid_type.right_type)
        else:
            self.valid_params.append(type(valid_type))

    def has_type(self, param_type):
        return param_type in self.valid_params

    def __repr__(self):
        return f'Address: at: {self.address}, params: ({self.valid_params})'


class Contract(Tezos):
    def __init__(self, address):
        assert isinstance(address, Address)
        self.value = value


class Key():
    pass

class KeyHash():
    pass

class Signature():
    pass
