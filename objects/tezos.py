class Tezos:
    def __init__(self, value):
        self.value = value

    value = None
    def __hash__(self):
        return hash(self.value)
    def __eq__(self, other):
        return self.value == other.value

    @property
    def type(self):
        return type(self)
