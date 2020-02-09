# discordbot
Discord bot to listening to Twitch streaming events to post them to designated channels

# Requirements
* Due to discord's client not support 3.4 or lower, you must have Python 3.5.3 or higher

# Supporting Docs
* Python Client: https://discordpy.readthedocs.io/en/latest/index.html

# Register a bot with Discord
* https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro

# Install & Setup

## Install Necessary Packages
```
pip3 install requirements.txt
sudo apt install postgresql
```

## Setup
* Create a config.yaml file with the following example:
```
app:
    hash: "Bot Hash & Number", (example: #1234)
    id: Bot's Unique Discord ID
    name: Bot's Name
    permissions: Bot's Required Permission Level (example: 84992)
    token: "Bot's token"

database:
    username: DB username
    password: DB password
    host: IP
    port: Port
    salt_file: Location of salt file
    sqlalchemy_uri: postgresql://{username}:{password}@{host}:{port}/{database}

logging:
    version: 1
    disable_existing_loggers: false
    formatters:
        base:
            format: "%(asctime)s [%(levelname)s] %(name)s:%(message)s"
    handlers:
        stream:
            class: logging.StreamHandler
            formatter: base
            level: DEBUG
        errors:
            class: logging.handlers.RotatingFileHandler
            level: ERROR
            formatter: base
            filename: error.log
            maxBytes: 52428800
            backupCount: 20
            encoding: utf8
    root:
        handlers: [stream, errors]
        level: DEBUG
```
* Create postgres user and setup DB
```
sudo passwd postgres
su - postgres
psql
\password postgres

CREATE DATABASE <bot's username>;
CREATE USER <bot's username>;
GRANT ALL PRIVILEGES ON DATABASE <bot's username> TO <bot's username>;
\password <bot's username>
```
* Run the bot with `python3 bot.py`