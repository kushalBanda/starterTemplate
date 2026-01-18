from typing import Self
from sqlalchemy.ext.asyncio import AsyncSession
from ..core.engine import get_sessionmaker
from ..configuration.types import AsyncSessionMaker


class UnitOfWork:
    """
    Unit of Work pattern for managing transactional boundaries.
    
    This context manager ensures that all database operations within its scope
    are atomic. It automatically commits the transaction on success and rolls
    back on exception.
    
    Usage:
        async with UnitOfWork() as session:
            repo = UserRepository(session)
            await repo.create(user)
    """

    def __init__(self, sessionmaker: AsyncSessionMaker | None = None) -> None:
        self._sessionmaker = sessionmaker or get_sessionmaker()
        self.session: AsyncSession | None = None

    async def __aenter__(self) -> AsyncSession:
        """Open a new session and begin the transaction."""
        self.session = self._sessionmaker()
        return self.session

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: object | None,
    ) -> None:
        """
        Handle transaction completion.
        
        - If an exception occurs (exc_type is not None), rollback.
        - If success, commit.
        - Always close the session.
        """
        if self.session is None:
            return
            
        try:
            if exc_type is None:
                await self.session.commit()
            else:
                await self.session.rollback()
        finally:
            await self.session.close()

    async def begin(self) -> Self:
        """
        Explicitly begin a unit of work outside a context manager.
        Useful for when context managers are not applicable.
        """
        await self.__aenter__()
        return self

    async def end(self, exc: BaseException | None = None) -> None:
        """End a unit of work created via begin/end."""
        await self.__aexit__(type(exc) if exc else None, exc, None)