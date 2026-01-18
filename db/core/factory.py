from ..connectors.mysql import MySQLConnector
from ..connectors.postgres import PostgresConnector
from ..connectors.sqlite import SQLiteConnector
from .interface import DBConnector
from ..configuration.settings import DatabaseSettings, DatabaseType


def get_connector(settings: DatabaseSettings) -> DBConnector:
    """
    Factory function to return the appropriate DB connector.
    
    Args:
        settings: The database settings object containing the 'type' field.
        
    Returns:
        DBConnector: An instantiated connector for the requested database type.
        
    Raises:
        ValueError: If the database type is not supported.
    """
    match settings.type:
        case DatabaseType.POSTGRES:
            return PostgresConnector(settings)
        case DatabaseType.MYSQL:
            return MySQLConnector(settings)
        case DatabaseType.SQLITE:
            return SQLiteConnector(settings)
        case DatabaseType.CLICKHOUSE:
            # Placeholder for ClickHouse implementation
            raise NotImplementedError("ClickHouse connector not yet implemented")
        case _:
            raise ValueError(f"Unsupported database type: {settings.type}")