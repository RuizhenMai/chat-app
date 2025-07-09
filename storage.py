from model import Message, Bot, User, Chat


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
