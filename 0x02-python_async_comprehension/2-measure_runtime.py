#!/usr/bin/env python3
"""Module that on how to use asyncio.gather to run coroutines in parallel."""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.time() - start_time
