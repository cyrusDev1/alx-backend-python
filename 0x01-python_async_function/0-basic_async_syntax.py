#!/usr/bin/env python3
import random
import asyncio
"""Write an asynchronous coroutine"""


async def wait_random(max_delay: int = 10) -> float:
    """return random number"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
