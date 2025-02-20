from openai import OpenAI

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
        self.prompt = "Answer the follwing question based on the context below:\nContext {}\nQuestion {}\nAnswer:"

    def generate(self, augmented_data):
        content = augmented_data["context"]
        query = augmented_data["query"]

        response = ""

        try:
            chat_response = self.client.chat.completions.create(
                    model=self.model_name,
                    temperature=0.1,
                    messages= [{"role" : "user", "content" : self.prompt.format(content, query)}]
                    )
            response = chat_response.choices[0].message.content.strip()

        except Exception as e:
            print(e)

        return response


