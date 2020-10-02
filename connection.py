import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect


def create_connection():
    """Create a database connection"""
    db_file = "data.db"

    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f"Connected to {sqlite3.version}")
        return connection
    except Error as SQLiteError:
        print(f"Error connecting to SQLite: {SQLiteError}")
