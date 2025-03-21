from openai import OpenAI
import os
from groq import Groq

class Generator:
    def __init__(self):
        pass

    def generate(self, augmented_data):
        raise RuntimeError("Not implemented")


class CorpusResponseGenerator:
    def __init__(self):
        super().__init__()

        self.client = OpenAI(
                base_url="http://localhost:11434/v1",
                api_key="Does not matter"
                )
        self.model_name = "deepseek-r1:7b"

        with open(os.path.join("prompts", "one.txt"), "r") as f:
            self.prompt = f.read().strip()


    def generate(self, augmented_data):
        content = augmented_data["context"]
        query = augmented_data["query"]

        response = ""
        content = self.prompt.format(content, query)

        try:
            chat_response = self.client.chat.completions.create(
                    model=self.model_name,
                    temperature=0.1,
                    messages= [{"role" : "user", "content" : content }]
                    )
            response = chat_response.choices[0].message.content.strip()

        except Exception as e:
            print(e)

        return response


class GroqResponseGenerator:
    def __init__(self, model_name="deepseek-r1-distill-llama-70b"):
        super().__init__()
        self.model_name = model_name

        self.client = Groq()

        with open(os.path.join("prompts", "one.txt"), "r") as f:
            self.prompt = f.read().strip()


    def generate(self, augmented_data):
        content = augmented_data["context"]
        query = augmented_data["query"]

        response = ""
        content = self.prompt.format(content, query)

        try:
            chat_response = self.client.chat.completions.create(
                    model=self.model_name,
                    temperature=0.6,
                    top_p=0.95,
                    max_completion_tokens=1024,
                    stream=False,
                    reasoning_format="raw",
                    messages= [{"role" : "user", "content" : content }]
                    )
            response = chat_response.choices[0].message.content.strip().replace("\n", "")

        except Exception as e:
            print(e)

        return response


