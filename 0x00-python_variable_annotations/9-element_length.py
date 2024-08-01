#!/usr/bin/env python3
"""Module that shows the annotation of an object in python. """


from collections.abc import Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> list[tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
