from constants import STORAGE_MODE
from fastapi import FastAPI
from service import ChatbotMessageSendService, ChatCoreService
from storage import MessageStore, ChatStore, UserStore, BotStore

# potentially dynamic import
from mem_storage_impl import (
    MemMessageStoreImpl,
    MemChatStoreImpl,
    MemUserStoreImpl,
    MemBotStoreImpl,
)
from mongo_storage_impl import (
    MongoMessageStoreImpl,
    MongoChatStoreImpl,
    MongoUserStoreImpl,
    MongoBotStoreImpl,
    MongoConnection,
)


def knitAllServices(app: FastAPI):
    msgStore: MessageStore = None
    chatStore: ChatStore = None
    userStore: UserStore = None
    botStore: BotStore = None
    if STORAGE_MODE == "mem":
        msgStore = MemMessageStoreImpl()
        chatStore = MemChatStoreImpl()
        botStore = MemBotStoreImpl()
        userStore = MemUserStoreImpl()
    elif STORAGE_MODE == "mongo":
        connection = MongoConnection()
        msgStore = MongoMessageStoreImpl(connection)
        chatStore = MongoChatStoreImpl(connection)
        botStore = MongoBotStoreImpl(connection)
        userStore = MongoUserStoreImpl(connection)

    else:
        raise NotImplementedError(f"{STORAGE_MODE} not implemented")

    chatCoreService = ChatCoreService(msgStore, chatStore, botStore, userStore)

    chatCoreService.prepareInitData()

    app.state.chatCoreService = chatCoreService
    app.state.chatbotMessageSendService = ChatbotMessageSendService(chatCoreService)
