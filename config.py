import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "1807893658:AAEvwn1MM_SKUpR2SbwHeHd4kgNvOsgHRcQ")
BOT_NAME = getenv("BOT_NAME", "DOPA-MUSIC")

API_ID = int(getenv("API_ID", "6664338"))
API_HASH = getenv("API_HASH", "ca633255509c018f2997e2ed8084f4cc")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1832447570").split()))


