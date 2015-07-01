import pytest

from src import check_balanced_parenthesis


balanced_strings = [
    'this (is [a {balanced} string]).',
    '()',
    '{}',
    '[]',
    '(){}[]',
    '({[]})',
    '',
]
unbalanced_strings = [
    '(',
    '{',
    '[',
    ')',
    '}',
    ']',
    '(}',
    '{]',
    '[)',
]
methods = [
    check_balanced_parenthesis.iterative,
    check_balanced_parenthesis.recursive,
]


@pytest.mark.parametrize(
    'input_str, method, expected',
    [
        (input_str, method, True)
        for input_str in balanced_strings
        for method in methods
    ] + [
        (input_str, method, False)
        for input_str in unbalanced_strings
        for method in methods
    ],
)
def test_by_parametrization(input_str, method, expected):
    assert method(input_str) == expected
