from pymongo import MongoClient

class MongoDBClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 27018
        self.database = 'blockchain'
        self.username = 'dev'
        self.password = 'dev'
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(self.host, self.port, username=self.username, password=self.password)
        self.db = self.client[self.database]

    def add_data(self, collection, data):
        self.db[collection].insert_one(data)

    def get_data(self, collection, query):
        return self.db[collection].find(query)

