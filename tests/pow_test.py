import pytest

from src import pow as _pow


methods = [
    _pow.pow_derpy,
    _pow.pow_better,
]


base_numbers = [2, 3, 5, 8, 11]
power_numbers = [2, 3, 5, 6, 7, 9, 11, 13, 15, 16]


@pytest.mark.parametrize(
    'base, power, method',
    [
        (x, y, method)
        for x in base_numbers
        for y in power_numbers
        for method in methods
    ],
)
def test_pow(base, power, method):
    assert base**power == method(base, power)
