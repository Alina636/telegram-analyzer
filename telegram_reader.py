# telegram_reader.py
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import os
import re

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient('anon', api_id, api_hash)


def extract_channel_username(link: str) -> str:
    match = re.search(r"t(?:elegram)?\.me\/(.+)", link)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Telegram channel link")


def get_channel_messages(channel_link: str, limit: int = 50):
    username = extract_channel_username(channel_link)
    with client:
        entity = client.get_entity(username)
        history = client(GetHistoryRequest(
            peer=entity,
            limit=limit,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0
        ))
        return [msg.message for msg in history.messages if msg.message]
