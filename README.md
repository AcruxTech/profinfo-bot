#  Telegram bot template (Aiogram 2.x)

There is the source code of the telegram bot template with explanations and installation instructions

- Features
- Project struct
- Installation (Ubuntu 18.04)

## Features

- FSM support
- Callback`s proccessing
- Logging
- Storing the token in environment variables

## Project struct

```
│   bot.service                 # move to /lib/systemd/system
│   main.py
│   requirements.txt
│
└───app
    ├───config                  # configuration files (with dataclasses)
    │       .env                # env`s file with token (DON`T PUBLISH TO OWN GITHUB)
    │       config.py
    │
    ├───handlers                # handlers (including callbacks)
    │       callbacks.py
    │       common.py
    │
    ├───states                  # available bot`s states
    │       MyState.py
    │
    └───utils                   # auxiliary funcs/classes
            functions.py
            keyboards.py
```

## Installation (Ubuntu 18.04)

This instruction requires ubuntu 18.04 (!) to run.

1. Update _sudo_ and install the python3.

```sh
sudo apt update
sudo apt -y upgrade
python3 -V
sudo apt install -y python3-pip
sudo apt install -y python3-venv
```

2. Create dir and venv

```sh
mkdir bot
cd bot
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements and deacivate venv

```sh
pip install -r requirements.txt
dectivate
```

4. Сreating a service file for continuous operation of the bot

```sh
nano /lib/systemd/system/bot.service        # see the service file in the repository
systemctl enable bot
systemctl start bot
systemctl status bot
```