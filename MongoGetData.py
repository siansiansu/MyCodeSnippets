from config.MongoDBClient import MongoDBClient
import json
import urllib.parse
import pandas as pd
from pandas.io.json import json_normalize
from bson import json_util

class MongoDBConnector(object):
    def __init__(self):
        self.db = MongoDBClient().db
        self.collection = "web_event"
        
        self.query = {"date": "2018-08-31", "e": "pageview"}
        self.projection = {"_id": 0, "kv.id": 1}
    
    def CursorFind(self):
        cnx = self.db[self.collection]
        cursor = cnx.find(self.query, self.projection)
        return cursor

class DataWasher(object):
    def __init__(self, cursor):
        self.cursor = cursor

    def mongoFlatten(self):
        sanitized = json.loads(json_util.dumps(self.cursor))
        normalized = json_normalize(sanitized)
        df = pd.DataFrame(normalized)
        return df

def main():
    f = MongoDBConnector()
    cursor = f.CursorFind()
    df = DataWasher(cursor).mongoFlatten()
    print(df)


if __name__ == "__main__":
    main()


