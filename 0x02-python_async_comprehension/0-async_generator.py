#!/usr/bin/env python3
"""Module on how to create async generators."""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a random float every time a loop is finished."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
