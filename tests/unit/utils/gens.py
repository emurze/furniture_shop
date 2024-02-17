import itertools
from collections.abc import Iterator


def id_gen() -> Iterator[int]:
    return itertools.count(1)
