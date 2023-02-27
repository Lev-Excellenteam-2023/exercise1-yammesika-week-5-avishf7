import functools


def join(*lists, sep='-'):
    """Concatenate lists using a separator and return as string."""
    if not lists:
        return None

    return functools.reduce(lambda x, y: x + [sep] + y, lists)


print(join([1, 2], [8], [9, 5, 6]))
