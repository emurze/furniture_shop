import functools
import inspect
from collections.abc import AsyncIterator, Callable
from contextlib import asynccontextmanager, suppress
from typing import AsyncGenerator, Any


async def _open_kw_gens(kw: dict) -> tuple[dict, list[AsyncGenerator]]:
    gens = []
    flat_kw = {}

    for key, value in kw.items():
        if inspect.isasyncgenfunction(value):
            async_gen = value()
            flat_kw[key] = await anext(async_gen)
            gens.append(async_gen)
        else:
            flat_kw[key] = value

    return flat_kw, gens


async def _close_gens(gens: list[AsyncGenerator]) -> None:
    for gen in gens:
        with suppress(StopAsyncIteration):
            await anext(gen)


@asynccontextmanager
async def iterate_kw_gens(kw: dict) -> AsyncIterator[dict]:
    flat_kw, gens = await _open_kw_gens(kw)
    yield flat_kw
    await _close_gens(gens)


def inject(**injected_kw) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def inner(*args, **kwargs) -> Any:
            async with iterate_kw_gens(injected_kw) as flat_kw:
                res = await func(*args, **flat_kw, **kwargs)

            return res

        return inner

    return wrapper
