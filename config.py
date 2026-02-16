# config.py
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "001.1437888022.3631660453:89260744027")
API_URL_BASE = os.getenv("API_URL_BASE", "https://api.armgs.team/bot/v1")
IS_MYTEAM = os.getenv("IS_MYTEAM", "1") == "1"

SEND_GENERIC_ERROR_TO_USER = True
