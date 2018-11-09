import pymysql

class SQLClient(object):

    def __init__(self, host="10.100.0.10", user="user", 
                       password="12345678", db="events"):

        self.connection = pymysql.connect(host=host, user=user, 
                                          password=password, 
                                          db=db, autocommit=True)