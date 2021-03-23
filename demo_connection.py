# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : demo_connection.py
@Author     : chuan.zhang
@Email      : chuan.zhang@outlook.com
@CreatedOn  : 2021/3/23 15:30
--------------------------------------
"""
from postgresql_utils import PgUtils


def main():
    db_cfg = {
        "database": "maixiaochai_db",
        "username": "maixiaochai",
        "password": "maixiaochai",
        "host": "localhost",
        "port": 5432
    }

    db = PgUtils(**db_cfg)
    sql = "select now()"
    data = db.fetchone(sql)
    print(data)


if __name__ == '__main__':
    main()
