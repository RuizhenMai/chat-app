from Storage import BotStore, ChatStore, UserStore, MessageStore
from pymongo import MongoClient
from constants import MONGO_ENDPOINT


class Connection:
    def __init__(self):
        self.connection = None

    def getConnection(self):
        if self.connection is None:
            self.connection = MongoClient(MONGO_ENDPOINT)

        return self.connection
