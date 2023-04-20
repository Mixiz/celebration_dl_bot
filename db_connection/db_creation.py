import sqlite3
from db_connection.db_connection import sql_exec, get_db_connection


# Create new database
def create_db():
    try:
        sqlite_connection = get_db_connection()
        print("SQLite DB is created successfully")

        sqlite_select_query = "select sqlite_version();"
        record = sql_exec(sqlite_select_query)
        print("SQLite Version: ", record)
    except sqlite3.Error as error:
        print("SQLite Connection Error", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


# Create Table Users
def create_user_table():
    create_table_query = """CREATE TABLE if not exists users (
      user_id int PRIMARY KEY,
      name TEXT,
      day int,
      month int,
      year int
    );
    """
    sql_exec(create_table_query)
    print("Created Table 'Users' ")
