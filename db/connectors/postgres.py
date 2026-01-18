from sqlalchemy.engine import URL

from ..core.interface import DBConnector


class PostgresConnector(DBConnector):
    """
    Postgres connector implementation using asyncpg.
    
    Compatible with:
    - PostgreSQL
    - Supabase (via PostgreSQL interface)
    - Any other PostgreSQL-wire compatible database
    """

    def get_url(self) -> URL:
        """Create a SQLAlchemy URL for asyncpg."""
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.settings.user,
            password=self.settings.password,
            host=self.settings.host,
            port=self.settings.port,
            database=self.settings.name,
        )