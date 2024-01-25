import pytest
from sqlalchemy.ext.asyncio import AsyncEngine


@pytest.mark.parametrize(
    "attribute, value",
    (
        ("driver", "asyncpg"),
        ("name", "postgresql"),
    )
)
async def test_engine(engine: AsyncEngine, attribute: str, value: str) -> None:
    assert getattr(engine, attribute) == value
