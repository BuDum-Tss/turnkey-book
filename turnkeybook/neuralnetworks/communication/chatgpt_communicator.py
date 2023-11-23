from openai import OpenAI

from .communicator import Communicator

OPENAI_API_KEY = "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"
ORGANIZATION_ID = "org-hN2FhFNtc0nRdPnHtlWvcJpx"


class ChatGPTCommunicator(Communicator):
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY, organization=ORGANIZATION_ID)

    def request(self, text: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", f"content": f"{text}"}
            ]
        )
        return completion.choices[0].message
