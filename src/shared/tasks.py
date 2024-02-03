import asyncio
from collections.abc import Callable
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from typing import Any


async def create_cpu_task(func: Callable, *args) -> Any:
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        return await loop.run_in_executor(executor, func, *args)


async def sync_to_async(func: Callable, *args) -> Any:
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as executor:
        return await loop.run_in_executor(executor, func, *args)
