from pydantic import BaseModdel
from constants import PROMPT_SAFETY_PREFIX


class ChatRequestBody(BaseModdel):
    memory: str = ""
    prompt: str = PROMPT_SAFETY_PREFIX
    bot_name: str = "bot"
    user_name: str
    chat_history: list[dict[str, str]]


class Message:
    sender: str
    messaage: str
