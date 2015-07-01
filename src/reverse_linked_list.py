"""
Reverse a linked list.
Do it in place.
"""


class Node(object):
    def __init__(self, datum, next_element=None):
        self.datum = datum
        self.next_element = next_element

    def __repr__(self):
        if self.next_element is None:
            return u'Node({datum})'.format(datum=self.datum)
        return u'Node({datum}, next_element={next_element})'.format(
            datum=self.datum,
            next_element=repr(self.next_element),
        )


def reverse_linked_list_in_place(first_node):
    this_node = first_node

    def helper(this_node, next_node):
        if next_node is None:
            return this_node

        if next_node.next_element is None:
            next_node.next_element = this_node
            return next_node

        next_next_node = next_node.next_element
        next_node.next_element = this_node

        return helper(next_node, next_next_node)

    reversed_first = helper(this_node, this_node.next_element)
    first_node.next_element = None

    return reversed_first
