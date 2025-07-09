from storage import BotStore, ChatStore, UserStore, MessageStore
from model import Bot, Chat, User, Message
from pymongo import MongoClient
from constants import MONGO_ENDPOINT, MONGO_PASSWORD


class MongoConnection:
    def __init__(self):
        self.connection: MongoClient = None

    def getConnection(self):
        if self.connection is None:
            self.connection = MongoClient(MONGO_ENDPOINT.format(MONGO_PASSWORD))

        return self.connection["chat_app"]


class MongoBotStoreImpl(BotStore):
    def __init__(self, mongoConnection: MongoConnection):
        self.collection = mongoConnection.getConnection()["bot"]

    def save(self, bot: Bot):
        self.collection.update_one(
            {"id": bot.id}, {"$set": bot.model_dump()}, upsert=True
        )

    def get(self, botId: int) -> Bot:
        res = self.collection.find_one({"id": botId})
        if res is None:
            raise IndexError(f"{botId} not in the store")

        return Bot(**res)


class MongoChatStoreImpl(ChatStore):
    def __init__(self, mongoConnection: MongoConnection):
        self.collection = mongoConnection.getConnection()["chat"]

    def save(self, chat: Chat):
        self.collection.update_one(
            {"id": chat.id}, {"$set": chat.model_dump()}, upsert=True
        )

    def get(self, chatId: int) -> Chat:
        res = self.collection.find_one({"id": chatId})
        if res is None:
            raise IndexError(f"{chatId} not in the store")
        return Chat(**res)


class MongoUserStoreImpl(UserStore):
    def __init__(self, mongoConnection: MongoConnection):
        self.collection = mongoConnection.getConnection()["user"]

    def save(self, user: User):
        self.collection.update_one(
            {"id": user.id}, {"$set": user.model_dump()}, upsert=True
        )

    def get(self, userId: int) -> User:
        res = self.collection.find_one({"id": userId})
        if res is None:
            raise IndexError(f"{userId} not in the store")
        return User(**res)


class MongoMessageStoreImpl(MessageStore):
    def __init__(self, mongoConnection: MongoConnection):
        self.collection = mongoConnection.getConnection()["message"]

    def append(self, message: Message):
        self.collection.insert_one(message.model_dump())

    def get(self, chatId: int, limit: int = 100) -> list[Message]:
        return [Message(**x) for x in self.collection.find({"id": chatId}).limit(limit)]
