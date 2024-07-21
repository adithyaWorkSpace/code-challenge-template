from psycopg2.extensions import connection as _connection
from typing import Generator
from contextlib import contextmanager
from django_project.dbconfig import dbparams

import psycopg2


@contextmanager
def get_db_connection() -> Generator[_connection, None, None]:
    """
    Provides a database connection using a context manager.

    Yields:
        _connection: A psycopg2 database connection.
    """
    connection = psycopg2.connect(**dbparams)
    try:
        yield connection
    finally:
        connection.close()
