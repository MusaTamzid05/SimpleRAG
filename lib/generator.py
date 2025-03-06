from openai import OpenAI
import os

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
        print(content)

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


