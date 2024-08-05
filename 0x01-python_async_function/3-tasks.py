#!/usr/bin/env python3
"""Module about a function that creates async tasks."""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[str]:
    """Returns an async task object."""
    return asyncio.create_task(wait_random(max_delay))
