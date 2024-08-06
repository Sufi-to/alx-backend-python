#!/usr/bin/env python3
"""Module on how to create async generators."""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
