from .tezos import Tezos
from .basic_types import Unit
from .tezos_types import Or


class Address(Tezos):
    def __init__(self, address=None, parameters=None, storage=None):
        self.address = address
        self.parameters = parameters
        self.storage = storage
        self.valid_params = []

    def update_address(self, address):
        self.address = address

    def update_parameters(self, params):
        self.parameters = params
        self.add_type(params)

    def update_storage(self, storage):
        self.storage = storage

    def add_type(self, valid_type):
        if isinstance(valid_type, Or):
            self.add_type(valid_type.left_type)
            self.add_type(valid_type.right_type)
        else:
            self.valid_params.append(valid_type)

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
