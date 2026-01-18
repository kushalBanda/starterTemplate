from typing import Any
from sqlalchemy.engine import URL
from ..core.interface import DBConnector


class SQLiteConnector(DBConnector):
    """
    SQLite connector implementation using aiosqlite.
    
    Useful for local development and testing.
    """

    def get_url(self) -> URL:
        """
        Create a SQLAlchemy URL for aiosqlite.
        Note: self.settings.name is used as the database file path.
        """
        return URL.create(
            drivername="sqlite+aiosqlite",
            database=self.settings.name,
        )

    def get_engine_args(self) -> dict[str, Any]:
        return {
            "pool_pre_ping": True,
        }