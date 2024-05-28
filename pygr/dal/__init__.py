from contextlib import closing
from pygr.common import DB_PASSWORD_DEV, DB_HOST_DEV, DB_PORT_DEV, DB_USER_DEV, DB_NAME
import psycopg2
from psycopg2 import connection


class DataBase:
    def __init__(self):
        self.initialize_database()

    def initialize_table(self, table_name, columns: dict):  # columns: dict->{<colum_name>:<data_type_and_restrictions>}
        with closing(self.get_connection().cursor()) as cur:
            sql = f"CREATE TABLE {table_name} ("
            for column_name, column_type in columns.items():
                sql += f"{column_name} {column_type},"
            sql = sql.rstrip(",") + ")"
            cur.execute(sql)

    def does_table_exists(self, table_name):
        query = "SELECT name FROM sqlite_master WHERE type = 'table' and name = ?"
        with closing(self.get_connection().cursor()) as cur:
            return len(cur.execute(query, [table_name]).fetchall()) > 0

    def initialize_database(self):
        conn = self.get_connection()
        conn.close()

    def get_connection(self) -> connection:
        try:
            return psycopg2.connect(database=DB_NAME,
                                    host=DB_HOST_DEV,
                                    user=DB_USER_DEV,
                                    password=DB_PASSWORD_DEV,
                                    port=DB_PORT_DEV)
        except Exception as e:
            print("Error creating connection to db")
            raise e

    def drop_table(self, table_name):
        with closing(self.get_connection().cursor()) as cur:
            cur.execute(f"DROP TABLE {table_name}")

    # columns is a dict like {<column name>: <column datatype>, <column name>: <column datatype>, ...}
    def create_table(self, table_name, columns):
        with closing(self.get_connection().cursor()) as cur:
            columns_definitions = ""
            for key, value in columns:
                columns_definitions += f"{key} {value},"
            cur.execute(f"CREATE TABLE ? ({columns_definitions.rstrip(',')})", [table_name])

    def insert_into_table(self, table_name, values):  # values: list->[value1: tpl, value2: tpl, ...]
        query = f"INSERT INTO {table_name} VALUES ("
        for _ in values[0]:
            query += "?,"
        query = query.rstrip(",") + ")"
        conn = self.get_connection()
        with closing(conn.cursor()) as cur:
            print(values, query)
            cur.executemany(query, values)
            conn.commit()

    def print_table(self, table_name):
        with closing(self.get_connection().cursor()) as cur:
            print(cur.execute(f"SELECT * FROM {table_name}").fetchall())
