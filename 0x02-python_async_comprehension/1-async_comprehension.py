#!/usr/bin/env python3
"""Module that shows how async comprehensions be used."""


import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns a list of floats created by the async request."""
    return [i async for i in async_generator()]
