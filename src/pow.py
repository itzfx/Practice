def pow_derpy(x, k):
    """A derpy, O(k) version."""
    if k == 1:
        return x
    if k == 0:
        return 1

    return x * pow_derpy(x, k - 1)


def pow_better(x, k):
    """A bit better, O(log(k)) version."""
    if k == 1:
        return x
    if k == 0:
        return 1

    if k % 2 == 1:
        return x * pow_better(x, k - 1)
    else:
        return pow_better(x * x, k / 2)
