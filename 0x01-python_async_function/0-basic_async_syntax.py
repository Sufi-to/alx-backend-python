#!/usr/bin/env python3
"""Module for getting accustomed using asyncio in python."""


import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Returns random float, makes the program delay by the same amount."""
    import random
    x: float = (random.random() * max_delay) + 1
    await asyncio.sleep(x)
    return x
