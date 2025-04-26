import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
Ты — опытный маркетолог-аналитик. Твоя задача — проанализировать Telegram-канал и дать рекомендации по маркетинговому улучшению.
Анализируй по следующим пунктам:
1. Кто целевая аудитория канала?
2. Есть ли признаки воронки продаж?
3. Что можно усилить в контенте и оформлении?
4. Общая оценка канала как маркетолога: сильные и слабые стороны

Основывайся на следующем:
- Название канала
- Описание
- Закреплённые сообщения
- Последние посты

Представь результат в виде красиво оформленного текста с заголовками, абзацами и пунктами.
"""

def analyze_messages(messages: list[str]) -> str:
    messages_joined = "\n\n".join(messages[-30:])  # анализируем последние 30 сообщений
    user_prompt = f"Вот пример содержания Telegram-канала:\n\n{messages_joined}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message["content"]
