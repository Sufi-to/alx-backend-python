#!/usr/bin/env python3
"""Module that on how to use asyncio.gather to run coroutines in parallel."""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return a float of how long the operation took."""
    start_time = time.time()
    gather_asyncs = [async_comprehension() for i in range(4)]
    results = await asyncio.gather(*gather_asyncs)
    return time.time() - start_time
