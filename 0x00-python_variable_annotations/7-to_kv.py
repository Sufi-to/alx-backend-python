#!/usr/bin/env python3
""""""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """Returns a tuple of str and float by combining the arguments."""
    return (k, (v**2))
