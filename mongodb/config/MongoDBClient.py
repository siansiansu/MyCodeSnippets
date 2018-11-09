from pymongo import MongoClient

class MongoDBClient(object):
    def __init__(self, host="10.100.0.10:3306", username="user", 
                 password="123456", authSource="events", 
                 authMechanism="SCRAM-SHA-1"):
                 
        self.client = MongoClient(host=host, 
                                  username=username, 
                                  password=password, 
                                  authSource=authSource, 
                                  authMechanism=authMechanism)
        
        self.db = self.client["events"]