from openai import OpenAI

from client_mood_track_api.config import (
    OPENAI_ORGANIZATION_ID,
    OPENAI_API_KEY,
    PROMPT_OPENAI,
)


class OpenAi:

    def __init__(self):
        pass

    def analyze_comment_ai(self, data):
        user_name = data.get("userName")
        print(f"Analyzing {user_name}`s comment")
        # implement chat gpt api

        print(f"API Key: {OPENAI_API_KEY}")
        print(f"Organization ID: {OPENAI_ORGANIZATION_ID}")

        client = OpenAI(api_key=OPENAI_API_KEY, organization=OPENAI_ORGANIZATION_ID)
        prompt = f"{PROMPT_OPENAI} {data}"

        analyzed_data = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", f"content": {prompt}}],
            stream=False,
        )

        return analyzed_data.choices[0].message["content"]
