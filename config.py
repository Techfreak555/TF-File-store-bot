import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN",8217472273:AAFPC6PlCi3U7BHT6Oh7F8dGVt3A3CF84ew "")
API_ID = int(os.environ.get("API_ID",25385750 ""))
API_HASH = os.environ.get("API_HASH", 77f0188ba2c26341834f248a0515840c"")


OWNER_ID = int(os.environ.get("OWNER_ID", "6299192020"))
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "Tecfreaktamil")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003094784222"))

FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1003056865925"))

FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "0-1002874243203"))

FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "0-1002836701968"))

FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "0"))

START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/ufzpkn.jpg")
F_PIC = os.environ.get("FORCE_PIC", "https://files.catbox.moe/ufzpkn.jpg")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


PORT = os.environ.get("PORT", "8050")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6299192020 ,6016699737, 5000956033]
    for x in (os.environ.get("ADMINS", "6299192020").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Sry You can't Able to Message me !\n\n» My Owner 👉 "

START_MSG = os.environ.get("START_MESSAGE", "<b>Hi {first} Friend I am a Advance File Store bot 😈 \n\n I was created by 👉@Tech_freak_tamil </b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} You must join the given channels ..\n\n 𝐒𝐨 please join and  “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")




ADMINS.append(OWNER_ID)
ADMINS.append(6299192020)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

class Txt(object):
    about = f"""<b>😈 My Name :</b> <a href=''>[AW] File store bot 😈 </a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/tech_freak_tamil'>TFT BOTS</a>
<b>🛡️ :</b> <a href='https://t.me/+NITVxLchQhYzNGZl'>TFT Developer</a>
    
<b>😈 Bot Made By :</b> @tech_freak_tamil"""


# Tech freak 
# Don't Remove Credit!!!
# Telegram Channel @Tech_freak_tamil
# Developer @devilo7
