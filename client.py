from openai import OpenAI
from secure_key_manager import get_api_key  # Read the API key safely

def ask_openai(prompt):
    api_key = get_api_key("jarvis-codeword")  # Use the codeword, not the raw key

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
