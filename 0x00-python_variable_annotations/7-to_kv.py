#!/usr/bin/env python3
""""""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of str and float by combining the arguments."""
    return (k, (v**2))
