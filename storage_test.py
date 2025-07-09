import unittest
from storage import *

class TestMemMessageStore(unittest.TestCase):
    def test(self):
        store = MemMessageStore()
        msg = Message(chatId=1, sender="kevin", message="hi there")
        store.append(msg)

        msgs = store.get(1)
        self.assertEqual(msgs[0].message, "hi there")

        store.append(Message(chatId=1, sender="kevin", message="how is the weather today?"))

        msgs = store.get(1)
        self.assertEqual(len(msgs), 2)
        self.assertEqual(msgs[1].message, "how is the weather today?")

class TestMemChatStore(unittest.TestCase):
    def test(self):
        store = MemChatStore()
        store.save(Chat(id=0, userId1=0, userId2=1))
        chat = store.get(0)
        self.assertEqual(chat.id, 0)


if __name__ == '__main__':
    unittest.main()