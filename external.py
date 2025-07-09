from model import Message
from constants import PROMPT_SAFETY_PREFIX, API_ENDPOINT, API_TOKEN
from dataclasses import dataclass, field
import requests
from requests import HTTPError


@dataclass
class ChatRequest:
    user_name: str
    bot_name: str = "bot"
    chat_history: list[Message] = field(default_factory=lambda: [])


class ChatBotClient:
    def __init__(self):
        pass

    def send(self, req: ChatRequest) -> str:

        body = {
            "memory": "",
            "prompt": PROMPT_SAFETY_PREFIX,
            "bot_name": req.bot_name,
            "user_name": req.user_name,
            "chat_history": [dict(x) for x in req.chat_history],
        }
        headers = {"Authorization": API_TOKEN}

        resp = requests.post(API_ENDPOINT, headers=headers, json=body)
        if resp.status_code != 200:
            raise HTTPError(
                f"response is not 200, but {resp.status_code}, resp is {resp.text}"
            )

        respPayload = resp.json()
        if "model_output" not in respPayload:
            raise HTTPError(f"invalid response format, check payload: {respPayload}")

        return respPayload["model_output"]
