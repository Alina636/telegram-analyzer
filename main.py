# main.py
from fastapi import FastAPI, Request
from telegram_reader import get_channel_messages
from gpt_analyzer import analyze_messages
import os

app = FastAPI()

@app.post("/analyze")
async def analyze_channel(request: Request):
    data = await request.json()
    channel_link = data.get("channel")
    if not channel_link:
        return {"error": "No channel link provided"}

    try:
        messages = get_channel_messages(channel_link)
    except Exception as e:
        return {"error": f"Error reading Telegram channel: {str(e)}"}

    if not messages:
        return {"error": "Failed to get messages from channel"}

    try:
        analysis = analyze_messages(messages)
    except Exception as e:
        return {"error": f"Error analyzing content: {str(e)}"}

    return {"analysis": analysis}
