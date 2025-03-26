from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)

result = client.chat.completions.create(
    model="ft:gpt-4o-2024-08-06:personal:test:BFIwmiPA",
    messages=[
        {
            "role": "system",
            "content": "Ton job est de dire si une phrase est gentille ou non. Tu devras répondre oui si la phrase est gentille, non si la phrase ne l'est pas et ... sinon",
        },
        {"role": "user", "content": "Tu es laid"},
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "response",
            "schema": {
                "type": "object",
                "properties": {
                    "sentence": {"type": "string"},
                    "result": {"type": "integer"},
                },
                "required": ["sentence", "result"],
            },
        },
    },
)

print(result.choices[0].message.content)
