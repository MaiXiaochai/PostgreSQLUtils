# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : postgresql_utils.py
@Author     : chuan.zhang
@Email      : chuan.zhang@outlook.com
@CreatedOn  : 2021/3/23 14:52
--------------------------------------
"""
from psycopg2 import connect


class PgUtils:
    def __init__(self, database, username, password, host, port):
        self.conn = connect(database=database, user=username, password=password, host=host, port=port)
        self.curs = self.conn.cursor()

    def execute(self, sql, args=None):
        if args:
            self.curs.execute(sql, args)
        else:
            self.curs.execute(sql)

    def executemany(self, sql, args=None):
        if args:
            self.curs.executemany(sql, args)
        else:
            self.curs.executemany(sql)

    def fetchone(self, sql, args=None):
        self.execute(sql, args)
        return self.curs.fetchone()

    def fetchall(self, sql, args=None):
        self.execute(sql, args)
        return self.curs.fetchall()

    def __del__(self):
        self.curs.close()
        self.conn.close()
