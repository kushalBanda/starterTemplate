from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from ..core.engine import get_sessionmaker


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency that yields a single async session per request.
    
    This dependency manages the session lifecycle:
    1. Creates a new AsyncSession from the pool.
    2. Yields it to the request handler.
    3. Automatically closes the session after the request is finished.
    """
    sessionmaker = get_sessionmaker()
    async with sessionmaker() as session:
        yield session