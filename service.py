from storage import MessageStore, MemMessageStore


class ChatbotMessageSendService:
    def __init__(self):
        self.msgStore: MessageStore = MemMessageStore()

    def sendMsg(self, chatId: int, msgContent: str):
        pass
