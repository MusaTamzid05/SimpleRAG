from lib.retrival import CorpusRetrival
from lib.generator import CorpusResponseGenerator

class RAG:
    def __init__(self):
        pass

    def run(self):
        raise RuntimeError("Not implemented")



class CorpusRAG(RAG):
    def __init__(
            self,
            path,
            database_name,
            chunk_size=1000
            ):
        super().__init__()
        self.retrival = CorpusRetrival(
                database_name=database_name,
                path=path,
                chunk_size=chunk_size
                )
        self.generator = CorpusResponseGenerator()


    def run(self):
        running = True
        while running:
            prompt = input(">>> ")
            if prompt == "exit":
                running = False
                continue

            result = self.retrival.get(query_text=prompt, result_count=5)
            response_list = result["documents"][0]

            augmented_data = {
                    "query" : prompt,
                    "context" : "\n".join(response_list)
                    }
            response = self.generator.generate(augmented_data=augmented_data)
            print(f"[*] LLM => {response}")



