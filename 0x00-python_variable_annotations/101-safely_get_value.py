#!/usr/bin/env python3
"""Module for learning about TypeVar when usin annotations in python."""


from typing import Mapping, Union, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns the key value pairs in the dictionary or None."""
    if key in dct:
        return dct[key]
    else:
        return default
