def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif isinstance(n, int) and n >= 2:
        return fib(n - 1) + fib(n - 2)
    else:
        raise ValueError(
            "Invalid argument n: {}. ".format(n) +
            "Non-negative integer is expected."
        )


if __name__ == "__main__":
    fib_list = [0, 1, 1, 2, 3, 5, 8, 13]
    for i, _fib in enumerate(fib_list):
        assert _fib == fib(i)
