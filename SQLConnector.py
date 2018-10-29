from config.SQLClient import SQLClient

class SQLConnector(object):
    def __init__(self):
        self.connection = SQLClient().connection

    def insertData(self, data):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `test` (`sdkid`, `period_type`, `start_date`, `unique_view`) VALUES (%s, %s, %s, %s)"
                cursor.executemany(sql, self.data)
                cursor.execute('COMMIT;')
        finally:
            connection.close()

def main():
    f = SQLConnector() 
    f.insertData(data)


if __name__ == "__main__":
    main()