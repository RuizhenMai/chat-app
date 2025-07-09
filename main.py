from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager

from service import ChatbotMessageSendService, ChatCoreService


# Define an async context manager for the lifespan events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code goes here
    print("Application is starting up...")
    # You can perform initialization tasks, e.g., connect to a database
    chatCoreService = ChatCoreService()
    chatCoreService.prepareInitData()
    app.state.chatCoreService = chatCoreService
    app.state.ChatbotMessageSendService = ChatbotMessageSendService(chatCoreService)
    yield  # The application will run here
    # Shutdown code goes here (after the application shuts down)
    print("Application is shutting down...")

app = FastAPI(lifespan=lifespan)


class Content(BaseModel):
    message: str


@app.post("/chat")
def chatDefault(content: Content):
    return chat(chatId=0, content=content)


@app.post("/chat/{chatId}")
def chat(chatId: int, content: Content):
    msgSendService = app.state.ChatbotMessageSendService
    rsp = msgSendService.sendMsg(chatId, content.message)
    return {"rsp": rsp}
