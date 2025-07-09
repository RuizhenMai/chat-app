from storage import (
    MessageStore,
    BotStore,
    UserStore,
    ChatStore,
)
from external import ChatRequest, ChatBotClient
from model import Message, Bot, Chat, User
from dataclasses import dataclass


@dataclass
class ChatEntity:
    id: int
    userId1: int  # typically user
    userName1: str
    userId2: int  # typically bot
    userName2: str
    chatHistory: list[Message]


class ChatCoreService:
    def __init__(
        self,
        msgStore: MessageStore,
        chatStore: ChatStore,
        botStore: BotStore,
        userStore: UserStore,
    ):
        self.msgStore = msgStore
        self.chatStore = chatStore
        self.botStore = botStore
        self.userStore = userStore

    def get(self, chatId: int) -> ChatEntity:
        # fetch necessary info from db
        messages = self.msgStore.get(chatId)
        chat = self.chatStore.get(chatId)
        user = self.userStore.get(chat.userId1)
        bot = self.botStore.get(chat.userId2)

        # assemble
        return ChatEntity(
            id=chat.id,
            userId1=user.id,
            userName1=user.name,
            userId2=bot.id,
            userName2=bot.name,
            chatHistory=messages,
        )

    def persistNewMsgs(self, messages: list[Message]):
        for msg in messages:
            self.msgStore.append(msg)

    def prepareInitData(self):
        """write some init data into db"""
        self.userStore.save(User(id=0, name="kevin"))
        self.botStore.save(Bot(id=1, name="bot"))

        self.chatStore.save(Chat(id=0, userId1=0, userId2=1))


class ChatbotMessageSendService:
    def __init__(self, chatService: ChatCoreService):
        self.chatService = chatService
        self.chatClient = ChatBotClient()

    def sendMsg(self, chatId: int, msgContent: str) -> str:
        # fetch all necessary info from db
        chatEntity = self.chatService.get(chatId)

        # append new msg
        additionalMsg = Message(
            chatId=chatId, sender=chatEntity.userName1, message=msgContent
        )
        chatEntity.chatHistory.append(additionalMsg)

        # send msg
        req = ChatRequest(
            user_name=chatEntity.userName1,
            bot_name=chatEntity.userName2,
            chat_history=chatEntity.chatHistory,
        )
        botOutput = self.chatClient.send(req)

        # persist the chat
        self.chatService.persistNewMsgs(
            [
                additionalMsg,
                Message(
                    chatId=chatEntity.id, sender=chatEntity.userName2, message=botOutput
                ),
            ]
        )

        return botOutput
