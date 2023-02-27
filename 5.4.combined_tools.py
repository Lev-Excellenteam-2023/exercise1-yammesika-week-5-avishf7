def interleave(*iterables):
    """Return a new list interleaving the items from each iterable."""
    combinedlist = []

    for i in range(len(iterables[0])):
        for it in iterables:
            combinedlist.append(it[i])

    return combinedlist


def iterinterleave(*iterables):
    """Yield items interleaved from each iterable."""
    for i in range(len(iterables[0])):
        for it in iterables:
            yield it[i]


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))

for iterable in iterinterleave('abc', [1, 2, 3], ('!', '@', '#')):
    print(iterable)
