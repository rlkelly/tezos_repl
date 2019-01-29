class Tezos:
    value = None
    def __hash__(self):
        return hash(self.value)
    def __eq__(self, other):
        return self.value == other.value
