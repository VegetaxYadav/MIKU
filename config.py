import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME")
OWNER_ID = getenv("OWNER_ID")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/2f4a3f7641100183e16f6.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/1bde1bf9b22c534ea7aae.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Yunxvoid/MIKU")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/84fb8c1dc192501e2b8f7.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/9ec62123c24f0f8559de8.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/a17572db013448a29f5f4.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/c8a40f99c6bd0e73e7923.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/786181c325777948e3d2f.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/6a2eaa99cba1f7e7ed91f.jpg")
