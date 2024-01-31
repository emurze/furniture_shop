from dataclasses import dataclass
from typing import Self, Any

from asyncpg import create_pool
from asyncpg.pool import PoolConnectionProxy, Pool


@dataclass
class Connection:
    engine: 'DBAPIEngine'
    pool: Pool | None = None
    conn: PoolConnectionProxy | None = None
    _is_initialized: bool = False

    async def _initialize(self) -> None:
        """
        Creates connection pool
        """

        if not self.pool:
            self.pool = await create_pool(self.engine.dsn)
            self._is_initialized = True

    async def connect(self) -> Self:
        """
        Takes connection from connection pool
        """

        await self._initialize()
        self.conn = await self.pool.acquire()
        return self

    async def close(self) -> None:
        """
        Returns connection to connection pool
        """

        await self.pool.release(self.conn)

    async def __aenter__(self) -> Self:
        return await self.connect()

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

    async def execute(self, statement: str) -> Any:
        """
        Checks that connection is given, then executes it and gets result
        """

        assert self._is_initialized
        return await self.conn.fetch(statement)


@dataclass
class DBAPIEngine:
    dsn: str

    def connect(self) -> Connection:
        return Connection(self)


@dataclass(frozen=True, slots=True)
class DBAPI:
    engine: DBAPIEngine

    async def create_tables(self) -> None:
        print("DROP TABLE role")
        async with self.engine.connect() as conn:
            stmt = """
                DROP TABLE IF EXISTS role;
            """
            await conn.execute(stmt)

        print("CREATE TABLE role")
        async with self.engine.connect() as conn:
            stmt = """
                CREATE TABLE role (
                    id serial PRIMARY KEY,
                    name varchar(256)
                )
            """
            await conn.execute(stmt)

    async def insert_data(self) -> None:
        print("INSERT INTO role")
        async with self.engine.connect() as conn:
            stmt = """
                INSERT INTO role (name)
                VALUES ('Hi'), ('Hello'), ('Hey')
            """
            await conn.execute(stmt)

    async def select_data(self) -> None:
        print("SELECT * FROM role")
        async with self.engine.connect() as conn:
            stmt = """
                SELECT * FROM role
            """
            res = await conn.execute(stmt)

            print(f"{res=}")

