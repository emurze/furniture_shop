from sqlalchemy.ext.asyncio import AsyncSession


def test_order_line_mapper_can_load_lines(session: AsyncSession) -> None:
    print(session)
