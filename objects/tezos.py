class Tezos:
    value = None
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    @property
    def type(self):
        return type(self)
