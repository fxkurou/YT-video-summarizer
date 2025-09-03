import openai

from configs.openai import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def generate_summary(text: str, style: str) -> str:
    """
    Generate a summary of the given text in the specified style using OpenAI's GPT-4o-mini model.
    :param text:
    :param style:
    :return: Summary string
    """
    prompt = f"Summarize the following text in {style} style:\n\n{text}"
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content
