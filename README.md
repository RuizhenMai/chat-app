## Introduction
I coded a chatapp in Python FastAPI interacting with the chatai chat api with extensive implementation. To note, I added 
1. Dependency Injection, one can use in-mem storage or external mongodb storage
2. Extensive Storage Model, (user1:user2):chat is 1-to-N, meaning one conversation pair can have as many chats as possible

## Installation

```bash
pip install "fastapi[standard]"
pip install "pymongo[srv]==3.12"
```

## Run

### Configuration

In `constants.py`, fill in `API_TOKEN`. For `STORAGE_MODE`, it's either `mem` or `mongo`. If you're using mongodb as a storage, key in the `MONGO_PASSWORD` as well if it's not filled in.

### Start Service
```bash
fastapi dev main.py
```
### Usage
```bash
curl --location 'http://127.0.0.1:8000/chat' \
--header 'Content-Type: application/json' \
--data '{
    "message": "hi there how is the weather today?"
}'

# sample return 
{
    "data": " Hello! Today's weather is sunny with a high of 78°F (25.5°C) and a low of 55°F (12.7°C). There is virtually no chance of rain. Have a great day! ☀️*Continuing the conversation*"
}
```
One can simply send chat messages to the `/chat` api. For more advanced usage, check in the endpoints in `main.py` to create more chats across different bot names and user names. 


## Structure

```bash
├── README.md
├── constants.py # constants and config
├── external.py # external client, interacting with the chatai api
├── main.py # entrypoint and endpoints 
├── mem_storage_impl.py # in-mem storage impl
├── model.py # db dataclasses
├── mongo_storage_impl.py # mongo storage impl
├── service.py # all chat services
├── service_factory.py # factory to instantiate and knit all services
├── storage.py # storage interface
└── storage_test.py # storage test

```