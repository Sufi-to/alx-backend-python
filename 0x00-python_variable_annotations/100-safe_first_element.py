#!/usr/bin/env python3
"""Module to understand more about annotations."""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of the iterable."""
    if lst:
        return lst[0]
    else:
        return None