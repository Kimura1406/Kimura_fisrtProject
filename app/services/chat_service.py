from openai import OpenAI

from app.config import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_SYSTEM_PROMPT


class ChatServiceError(Exception):
    pass


def generate_reply(message: str) -> str:
    if not OPENAI_API_KEY:
        raise ChatServiceError("OPENAI_API_KEY is missing.")

    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=[
            {
                "role": "system",
                "content": OPENAI_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    reply = response.output_text.strip()
    if not reply:
        raise ChatServiceError("Model returned an empty response.")

    return reply
