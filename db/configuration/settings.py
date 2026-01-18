from enum import Enum
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseType(str, Enum):
    """Supported database types."""

    POSTGRES = "postgres"
    MYSQL = "mysql"
    CLICKHOUSE = "clickhouse"
    SQLITE = "sqlite"


class DatabaseSettings(BaseSettings):
    """Database settings derived from environment variables."""

    model_config = SettingsConfigDict(env_prefix="DB_", case_sensitive=False, frozen=True)

    type: DatabaseType = Field(default=DatabaseType.POSTGRES)
    host: str = Field(default="localhost")
    port: int = Field(default=5432)
    name: str = Field(default="app")
    user: str = Field(default="app")
    password: str = Field(default="")
    
    # Connection Pool Settings
    pool_size: int = Field(default=10)
    max_overflow: int = Field(default=20)
    pool_timeout_seconds: int = Field(default=30)
    pool_recycle_seconds: int = Field(default=1800)

    @classmethod
    def from_env(cls) -> "DatabaseSettings":
        """Build settings from the configured environment."""
        return cls()
