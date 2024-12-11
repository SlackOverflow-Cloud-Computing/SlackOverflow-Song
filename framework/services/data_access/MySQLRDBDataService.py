import pymysql
from .BaseDataService import DataDataService


class MySQLRDBDataService(DataDataService):
    """
    A generic data service for MySQL databases. The class implement common
    methods from BaseDataService and other methods for MySQL. More complex use cases
    can subclass, reuse methods and extend.
    """

    def __init__(self, context):
        super().__init__(context)

    def _get_connection(self):
        connection = pymysql.connect(
            host=self.context["host"],
            port=self.context["port"],
            user=self.context["user"],
            passwd=self.context["password"],
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return connection

    def get_data_object(self,
                        database_name: str,
                        collection_name: str,
                        key_field: str,
                        key_value: str):
        """
        See base class for comments.
        """

        connection = None
        result = None

        try:
            sql_statement = f"SELECT * FROM {database_name}.{collection_name} " + \
                        f"where {key_field}=%s"
            connection = self._get_connection()
            cursor = connection.cursor()
            cursor.execute(sql_statement, [key_value])
            result = cursor.fetchone()
        except Exception as e:
            print("error with db call")
            print(e)
            if connection:
                connection.close()

        return result

    def get_all_data_objects(self, database_name: str, collection_name: str):
        connection = None
        result = None

        try:
            sql_statement = f"SELECT * FROM {database_name}.{collection_name}"
            connection = self._get_connection()
            cursor = connection.cursor()
            cursor.execute(sql_statement)
            result = cursor.fetchall()
        except Exception as e:
            print("error with db call")
            print(e)
            if connection:
                connection.close()

        return result

    def get_count(self, database_name: str, collection_name: str) -> int:
        """Get total count of records in the table"""
        connection = None
        try:
            sql_statement = f"SELECT COUNT(*) as count FROM {database_name}.{collection_name}"
            connection = self._get_connection()
            cursor = connection.cursor()
            cursor.execute(sql_statement)
            result = cursor.fetchone()
            return result['count']
        except Exception as e:
            print("Error getting count:", e)
            return 0
        finally:
            if connection:
                connection.close()

    def get_paginated_data(self, database_name: str, collection_name: str, offset: int, limit: int):
        """Get paginated data from the table"""
        connection = None
        try:
            sql_statement = f"SELECT * FROM {database_name}.{collection_name} LIMIT %s OFFSET %s"
            connection = self._get_connection()
            cursor = connection.cursor()
            cursor.execute(sql_statement, (limit, offset))
            return cursor.fetchall()
        except Exception as e:
            print("Error with paginated db call:", e)
            return []
        finally:
            if connection:
                connection.close()

    def add_data_object(self,
                        database_name: str,
                        collection_name: str,
                        data: dict):
        connection = None
        success = False

        try:
            sql_statement = f"INSERT INTO {database_name}.{collection_name} " + \
                f"({', '.join(data.keys())}) " + \
                f"VALUES ({', '.join(['%s'] * len(data))})"
            sql_statement = sql_statement.replace("key", "`key`")
            connection = self._get_connection()
            cursor = connection.cursor()
            cursor.execute(sql_statement, list(data.values()))
            success = True
        except Exception as e:
            if connection:
                connection.close()
        return success
