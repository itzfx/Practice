import pytest

from src import reverse_linked_list
from src.reverse_linked_list import Node


methods = [
    reverse_linked_list.reverse_linked_list_in_place,
]


def generate_linked_list(num_elements=3):
    """Return the first node in a list of `num_elements`."""
    first_node = Node(1)

    # Make the rest of the nodes
    n = first_node
    for i in xrange(2, num_elements + 1):
        _n = Node(i)
        n.next_element = _n
        n = _n

    return first_node


def get_datums_as_list(first_node):
    datums = []

    n = first_node
    while (n is not None):
        datums.append(n.datum)
        n = n.next_element

    return datums


@pytest.mark.parametrize(
    'size, method',
    [
        (size, method)
        for size in [1, 3, 5, 7, 20]
        for method in methods
    ],
)
def test_reverse_linked_list(size, method):
    first_node = generate_linked_list(size)
    original_datums = get_datums_as_list(first_node)

    r = method(first_node)

    assert list(reversed(original_datums)) == get_datums_as_list(r)
