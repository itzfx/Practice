"""
Given an input array and a number X, return all pairs in A that would sum to X.
"""


def add_unordered_tuple_to_set(_set, _tuple):
    """Check if a 2-element tuple is in the set in reverse order before adding
    it. If it exists, don't bother adding it.

    Use this method when (x, y) ~= (y, x) for the purpose of the set.
    """
    x, y = _tuple
    if (y, x) in _set:
        return

    _set.add(_tuple)


def by_difference(array, pair_sum):
    found_pairs = set()

    for num in array:
        diff = pair_sum - num

        # Make a copy of the numbers and remove the one being checked so this
        # doesn't accidentally find a valid sum using the same element twice.
        numbers = list(array)
        numbers.remove(num)
        numbers = set(numbers)

        if diff in numbers:
            add_unordered_tuple_to_set(found_pairs, (num, diff))

    return found_pairs


def by_brute_force(array, pair_sum):
    found_pairs = set()
    for i in xrange(len(array)):
        for j in xrange(len(array)):
            # Don't accidentally count the same element twice
            if j == i:
                continue

            if array[i] + array[j] == pair_sum:
                add_unordered_tuple_to_set(
                    found_pairs,
                    (array[i], array[j]),
                )

    return found_pairs
