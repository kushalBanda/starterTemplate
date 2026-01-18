from abc import ABC, abstractmethod
from typing import Any

from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from ..configuration.settings import DatabaseSettings


class DBConnector(ABC):
    """
    Abstract interface for database connectors.
    
    Any new database backend must implement this class to ensure
    compatibility with the core engine factory.
    """

    def __init__(self, settings: DatabaseSettings) -> None:
        self.settings = settings

    @abstractmethod
    def get_url(self) -> URL:
        """Construct the SQLAlchemy URL for this connector."""
        pass

    def get_engine_args(self) -> dict[str, Any]:
        """
        Return engine-specific arguments (pooling, timeouts, etc.).
        
        Subclasses can override this to provide driver-specific options.
        """
        return {
            "pool_size": self.settings.pool_size,
            "max_overflow": self.settings.max_overflow,
            "pool_timeout": self.settings.pool_timeout_seconds,
            "pool_recycle": self.settings.pool_recycle_seconds,
            "pool_pre_ping": True,
        }

    def create_engine(self) -> AsyncEngine:
        """Create and return a configured SQLAlchemy AsyncEngine."""
        return create_async_engine(
            self.get_url(),
            **self.get_engine_args(),
        )