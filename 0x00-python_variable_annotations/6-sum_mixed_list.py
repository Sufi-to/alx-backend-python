#!/usr/bin/env python3
"""Module for adding elements in a list."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Sums all the elements in the list and returns a float."""
    return sum(mxd_lst)
