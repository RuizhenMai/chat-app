from model import Message, Bot, User, Chat
from collections import defaultdict


class MessageStore:
    def append(self, message: Message):
        """persist a message

        Args:
            chatId (int): chat id
            message (Message): message

        Raises:
            NotImplementedError: interface
        """
        raise NotImplementedError

    def get(self, chatId: int, limit: int = 100) -> list[Message]:
        """get a list of historic messages 

        Args:
            chatId (int): chat id
            limit (int, optional): number of messages to obtain. Defaults to 100.

        Raises:
            NotImplementedError: interface
        """
        raise NotImplementedError

class BotStore:
    def save(self, bot: Bot):
        raise NotImplementedError
    def get(self, botId: int) -> Bot:
        raise NotImplementedError
    
class UserStore:
    def save(self, user: User):
        raise NotImplementedError
    def get(self, userId: int) -> User:
        raise NotImplementedError
    
class ChatStore:
    def save(self, chat: Chat):
        raise NotImplementedError
    def get(self, chatId: int) -> Chat:
        raise NotImplementedError
    
class MemChatStore(ChatStore):
    def __init__(self):
        self.store = {}

    def save(self, chat:Chat):
        self.store[chat.id] = chat

    def get(self, chatId: int) -> Chat:
        if chatId not in self.store:
            raise IndexError(f"{chatId} not in the store")
        
        return self.store[chatId]


class MemMessageStore(MessageStore):
    def __init__(self):
        self.store = defaultdict(list)

    def append(self, message: Message):
        self.store[message.chatId].append(message)

    def get(self, chatId: int, limit: int = 100) -> list[Message]:
        if chatId not in self.store:
            self.store[chatId] = []

        return self.store[chatId][-limit:]

class MemBotStore(BotStore):
    def __init__(self):
        # int -> Bot
        self.store = {}

    def save(self, bot: Bot):
        self.store[bot.id] = bot
    
    def get(self, botId: int) -> Bot:
        if botId not in self.store:
            raise IndexError(f"{botId} not in the store")

        return self.store[botId]
    
class MemUserStore(UserStore):
    def __init__(self):
        # int -> user
        self.store = {}

    def save(self, user: User):
        self.store[user.id] = user
    
    def get(self, userId: int) -> User:
        if userId not in self.store:
            raise IndexError(f"{userId} not in the store")

        return self.store[userId]