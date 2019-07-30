def fib(n: int) -> int:
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif isinstance(n, int) and n >= 2:
        return fib(n - 1) + fib(n - 2)
    else:
        raise ValueError(
            "Invalid argument n: {}. ".format(n) +
            "Non-negative integer is expected."
        )
