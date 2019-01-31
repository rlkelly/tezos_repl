from .hash import check_signature

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
