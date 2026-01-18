from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from .engine import get_engine


async def check_database_health() -> bool:
    """
    Perform a lightweight check to verify database connectivity.
    
    Executes a simple 'SELECT 1' query against the configured database engine.
    
    Returns:
        bool: True if the database is reachable and responsive, False otherwise.
    """
    engine = get_engine()
    try:
        async with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))
        return True
    except SQLAlchemyError:
        return False