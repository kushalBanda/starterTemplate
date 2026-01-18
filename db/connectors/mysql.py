from sqlalchemy.engine import URL

from ..core.interface import DBConnector


class MySQLConnector(DBConnector):
    """MySQL connector implementation using aiomysql."""

    def get_url(self) -> URL:
        """Create a SQLAlchemy URL for aiomysql."""
        return URL.create(
            drivername="mysql+aiomysql",
            username=self.settings.user,
            password=self.settings.password,
            host=self.settings.host,
            port=self.settings.port,
            database=self.settings.name,
        )