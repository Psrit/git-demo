def fib(n: int) -> int:
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(
            "Invalid argument n: {}. ".format(n) +
            "Non-negative integer is expected."
        )

    _fib = []

    for i in range(n + 1):
        if i == 0:
            _fib.append(0)
        elif i == 1:
            _fib.append(1)
        else:
            _fib.append(
                _fib[-1] + _fib[-2]
            )

    return _fib[-1]
