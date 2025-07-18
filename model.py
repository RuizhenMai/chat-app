from pydantic import BaseModel


class Bot(BaseModel):
    id: int
    name: str


class User(BaseModel):
    id: int
    name: str


class Message(BaseModel):
    chatId: int  # the chat id that this message is associated with
    sender: str  # sender name
    message: str  # message content


class Chat(BaseModel):
    id: int
    userId1: int  # typically user
    userId2: int  # typically bot, we potentially should add TalkerType, one is bot the other is user
