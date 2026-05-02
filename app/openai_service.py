import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(question):
    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": "Act like a helpful personal assistant"},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
        max_output_tokens=512
    )
    return response.output_text.strip()


def summarize_email(email_text):
    prompt = f"Summarize the following email in 2-3 sentences: {email_text}"

    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": "Act like an expert email assistant"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_output_tokens=512
    )
    return response.output_text.strip()