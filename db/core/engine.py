from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from .factory import get_connector
from ..configuration.settings import DatabaseSettings
from ..configuration.types import AsyncSessionMaker

_engine: AsyncEngine | None = None
_sessionmaker: AsyncSessionMaker | None = None


def get_engine() -> AsyncEngine:
    """
    Return a singleton async engine configured for production use.
    
    The engine is lazily initialized on the first call using settings
    from the environment and the appropriate connector factory.
    """
    global _engine
    if _engine is None:
        settings = DatabaseSettings.from_env()
        connector = get_connector(settings)
        _engine = connector.create_engine()
    return _engine


def get_sessionmaker() -> AsyncSessionMaker:
    """
    Return a singleton sessionmaker bound to the shared engine.
    
    The sessionmaker produces 'AsyncSession' instances for database interactions.
    """
    global _sessionmaker
    if _sessionmaker is None:
        _sessionmaker = async_sessionmaker(
            bind=get_engine(),
            expire_on_commit=False,
            class_=AsyncSession,
        )
    return _sessionmaker


async def dispose_engine() -> None:
    """
    Close the engine and reset the pool.
    
    This should be called during application shutdown to ensure all connections
    are closed gracefully.
    """
    global _engine, _sessionmaker
    if _engine is not None:
        await _engine.dispose()
    _engine = None
    _sessionmaker = None
