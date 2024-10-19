from krathon.utils.db_util import create_dbconn_mysql


class BaseModel:
    def __init__(self):
        self.dbconn = None
        self.cursor = None

    def conn(self):
        if not self.cursor:
            if not self.dbconn:
                self.dbconn = create_dbconn_mysql()
            self.cursor = self.dbconn.cursor()

    def rollback(self):
        if self.dbconn:
            self.dbconn.rollback()

    def commit(self):
        try:
            self.dbconn.commit()
        except Exception as exc:
            self.rollback()
            raise Exception(f'db commit failed: {exc}')

    def begin(self):
        if self.dbconn:
            self.dbconn.begin()

    def close(self):
        try:
            if self.dbconn:
                if self.cursor:
                    self.cursor.execute('UNLOCK TABLES;')
                    self.cursor.close()
                self.dbconn.close()
        except Exception as exc:
            raise Exception(f'db close failed: {exc}')
        finally:
            self.cursor = None
            self.dbconn = None

    def execute(self, sql_str, values=None):
        try:
            self.cursor.execute(sql_str, values)
        except Exception as exc:
            self.rollback()
            self.close()
            raise Exception(f'db execute failed: {exc}')

    def executemany(self, sql_str, values=None):
        try:
            self.cursor.executemany(sql_str, values)
        except Exception as exc:
            self.rollback()
            self.close()
            raise Exception(f'db executemany failed: {exc}')
