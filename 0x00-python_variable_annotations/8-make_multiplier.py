#!/usr/bin/env python3
"""Module of a function that returns a another function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiples the float."""
    def inner_func(n: float) -> float:
        """Multiplies the float."""
        return n * multiplier
    return inner_func
