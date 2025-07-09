## Introduction

## Installation

```bash
pip install "fastapi[standard]"
```

## Run

### Configuration

In `constants.py`, fill in ...

```bash
fastapi dev main.py
```

## Structure

```bash
.
├── README.md
├── constants.py
├── external.py # clients, interaction with external services
├── main.py # entry, api endpoints
├── model.py # persistence model
├── service.py
├── storage.py # storage interface and definition
└── storage_test.py # storage test
```
