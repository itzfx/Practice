"""
Give a function that takes a string as an input and returns True if the
parenthesis in the input string are "balanced", which means that every closed
parenthesis is preceeded by a close parenthesis of the same type that has not
been matched. Non-parenthesis characters can be included in the string but do
not count towards the balancing.
"""


CLOSE_TO_OPEN_PARENTHESIS = {
    ')': '(',
    '}': '{',
    ']': '[',
}
OPEN_PARENS = set(CLOSE_TO_OPEN_PARENTHESIS.values())
CLOSE_PARENS = set(CLOSE_TO_OPEN_PARENTHESIS.keys())


def iterative(input_str):
    seen_open_parens = []
    for c in input_str:
        if c in OPEN_PARENS:
            seen_open_parens.append(c)
        if c in CLOSE_PARENS:
            if len(seen_open_parens) < 1:
                return False
            if CLOSE_TO_OPEN_PARENTHESIS[c] != seen_open_parens.pop():
                return False

    return len(seen_open_parens) == 0


def recursive(input_str):
    """This only exists to show how ridiculous it is to solve the problem with
    a... less than optimal solution.
    """
    class IncorrectParenthesis(Exception): pass
    class UnmatchedParenthesis(Exception): pass

    def find_next_unmatched_close_paren(index):
        i = index
        while i < len(input_str):
            if input_str[i] in OPEN_PARENS:
                ni, np = find_next_unmatched_close_paren(i + 1)

                if ni is None and np is None:
                    raise UnmatchedParenthesis()

                if CLOSE_TO_OPEN_PARENTHESIS[np] != input_str[i]:
                    raise IncorrectParenthesis()

                i = ni

            elif input_str[i] in CLOSE_PARENS:
                return i, input_str[i]

            i += 1

        # Not strictly necessary but I like having a consistent return type
        # (tuples).
        return None, None

    try:
        index, char = find_next_unmatched_close_paren(0)
        print index, char
        return index is None and char is None
    except (IncorrectParenthesis, UnmatchedParenthesis):
        return False
