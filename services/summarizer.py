import openai

from configs.openai import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def generate_summary(text: str, style: str) -> str:
    prompt = f"Summarize the following text in {style} style:\n\n{text}"
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content
