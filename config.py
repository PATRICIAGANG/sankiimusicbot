from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQB2SXDwsmA93uWvCYKlf-QAVGbQfASmmUSPQ2HxncXp5raB-h2isZonCkpwu_p36RMOHK5n0CDwqNE-jpHN4titj4hhhh9U53llAbZxdeBEW2e7aRcRd6I-SzSUVHC40dxSkYcEgVkzicTqinie2t0JsX8F32us4vG88yH-7DqYsA1aKJzjjqUO0yEjLq5Kx_iNLw6haRNkDvlwiDV-kcEogaHcBweaoRuVNxSO2-tYZxOOn2lyI1YaGuj5KfryICh5EeGaptp3sw668dp7xgxhVKK6pRQRGHbNIh3i57qXsVX3szEGZDA6VE1ZQJzBVfioxjaqen9TPGRC09euAHH4bPJMwAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1861430117:AAGr5rgu-AtR4ZjWX4NsXNWNWaQTendaSpc")
BOT_NAME = getenv("BOT_NAME", "PATRICIA")
admins = {}
API_ID = int(getenv("API_ID", "6443174"))
API_HASH = getenv("API_HASH", "301af3f1c45cf9c5908814c24fb7ab52")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "80"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1607847356").split()))
