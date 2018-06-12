import sqlite3
from settings import DB_NAME


class Connector:
    def __init__(self):
        self.name = DB_NAME
        self.conn = sqlite3.connect("{}.db".format(
                                            self.name))
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values):
        self.cursor.execute(query, values)
        self.conn.commit()

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get(self, query, id):
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()
