import os

from dotenv import load_dotenv
from openai import OpenAI

# Set your OpenAI API key from .env
load_dotenv()
api_key = os.getenv("api_key")

# Initialize the OpenAI API client
client = OpenAI(api_key=api_key)

result = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Ton job est de répondre à des questions concernant la géographie de manière poétique c'est à dire en rimes et en alexendrin. Si on te pose des questions autre que de la géographie répond que tu ne sais pas",
        },
        # {"role": "user", "content": "Quelle est la capitale de la France ?"},
        {"role": "user", "content": "Quelle est la température de fusion du fer ?"},
    ],
)
# print(result, end="\n")
print(
    result.choices[0].message.content
)  # extracting the content from the restult message
