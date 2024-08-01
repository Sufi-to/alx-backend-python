#!/usr/bin/env python3
"""Module that shows the annotation of an object in python. """


from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a tuple of the element and its length."""
    return [(i, len(i)) for i in lst]
