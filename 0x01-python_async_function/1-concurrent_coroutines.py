#!/usr/bin/env python3
"""Module that builds upon the previous exercise."""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of floats of all the delays."""
    res = [await wait_random(max_delay) for i in range(n)]
    return res
