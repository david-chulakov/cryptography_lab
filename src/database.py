from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession



class BaseTable(DeclarativeBase):

    repr_cols_num = 2
    repr_cols = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"{self.__class__.__name__}({', '.join(cols)}"
    


engine = create_async_engine(app_settings.DATABASE_URL)
session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def startup_db():
    async with engine.begin() as conn:
        await conn.run_sync(BaseTable.metadata.drop_all)
        await conn.run_sync(BBaseTablease.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session
