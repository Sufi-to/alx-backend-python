#!/usr/bin/env python3
"""Module for type checking."""


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list with the given elements printed by the factor. """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
