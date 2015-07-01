import pytest

from src import array_pair_sum


methods = [
    array_pair_sum.by_difference,
    array_pair_sum.by_brute_force,
]


@pytest.mark.parametrize('method', methods)
def test_exists(method):
    array = [1, 2, 3, 4]
    pair_sum = 6

    assert method(array, pair_sum) == set([(2, 4)])


@pytest.mark.parametrize('method', methods)
def test_duplicate_values(method):
    array = [3, 3, 4, 4]
    pair_sum = 6

    assert method(array, pair_sum) == set([(3, 3)])


@pytest.mark.parametrize('method', methods)
def test_multiple_exists(method):
    array = [1, 2, 3, 4]
    pair_sum = 5

    assert method(array, pair_sum) == set([(1, 4), (2, 3)])


@pytest.mark.parametrize('method', methods)
def test_no_solution(method):
    array = [1, 2, 3, 4]
    pair_sum = 8

    assert method(array, pair_sum) == set()
