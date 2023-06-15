import pymysql


class sqlUtils:

    def __init__(self):
        self.db = pymysql.Connect(
            host="localhost",
            user="liyl72",
            password="Liyinglong1121!",
            database="api_test"
        )
        self.cursor = self.db.cursor()
    '''
    用于增删改sql
    '''
    def sql_commit(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
            self.close()
            return False
        self.close()
        return True

    '''
    用于查所有行的sql
    '''
    def sql_fetch_all(self,sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.close()

    '''
        用于查单行的sql
        '''
    def sql_fetch_one(self, sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            self.close()


    def close(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    result = sqlUtils().sql_fetch_all("SELECT COUNT(*) FROM apiInfo")
    print(result)