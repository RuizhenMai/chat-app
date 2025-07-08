from model import Message
from collections import defaultdict


class MessageStore:
    def save(self, chatId: int, message: Message):
        raise NotImplementedError

    def get(self, chatId: int, limit: int = 100):
        raise NotImplementedError


class MemMessageStore(MessageStore):
    def __init__(self):
        self.store = defaultdict(list)

    def save(self, chatId: int, message: Message):
        self.store[chatId].append(message)

    def get(self, chatId: int, limit: int = 100) -> list[Message]:
        if chatId not in self.store:
            raise IndexError(f"{chatId} not in the store")

        return self.store[chatId][-100:]
