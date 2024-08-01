#!/usr/bin/env python3
"""Module for a key value argument and returns value sqaured along
the key in tuple."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of str and float by combining the arguments."""
    return (k, (v**2))
