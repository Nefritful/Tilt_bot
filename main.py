# main.py
from bot.bot import Bot
from bot.handler import MessageHandler

import time
import logging

import config
import texts
from log_setup import setup_logging

setup_logging("logging.ini")

log = logging.getLogger("tilt")
audit_log = logging.getLogger("tilt.audit")

bot = Bot(
    token=config.BOT_TOKEN,
    api_url_base=config.API_URL_BASE,
    is_myteam=config.IS_MYTEAM
)

def _safe_attr(obj, name, default=None):
    return getattr(obj, name, default)

def log_user_event(event):
    audit_log.info(
        "USER_EVENT chat=%s user=%s msg_id=%s ts=%s text=%r",
        _safe_attr(event, "from_chat"),
        _safe_attr(event, "from_user"),
        _safe_attr(event, "msg_id"),
        _safe_attr(event, "timestamp"),
        _safe_attr(event, "text"),
    )

def message_cb(bot, event):
    log_user_event(event)
    try:
        bot.send_text(chat_id=event.from_chat, text=texts.TEXT_HELLO)
        log.info("BOT_SEND chat=%s text=%r", event.from_chat, texts.TEXT_HELLO)
    except Exception:
        log.exception("ERROR while handling event")
        if config.SEND_GENERIC_ERROR_TO_USER:
            try:
                bot.send_text(chat_id=event.from_chat, text=texts.TEXT_GENERIC_ERROR)
            except Exception:
                log.exception("ERROR while sending generic error message")

bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
log.info("Bot started. Waiting for events...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    log.info("Stopped by KeyboardInterrupt")
