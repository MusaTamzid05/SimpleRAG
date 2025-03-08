from lib.retrival import CorpusRetrival
from lib.generator import CorpusResponseGenerator
from lib.retrival import IndexRetrival
from lib.retrival import WebRetrival
from lib.retrival import NaiveKeywordRetrival
from lib.retrival import NaiveVectorizeRetrival

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



class CorpusIndexRAG(RAG):
    def __init__(
            self,
            dir_path,
            chunk_size=1000
            ):
        super().__init__()
        self.retrival = IndexRetrival(
                dir_path=dir_path,
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

            retrived_list = self.retrival.get(query_text=prompt, result_count=5)

            augmented_data = {
                    "query" : prompt,
                    "context" : "\n".join(retrived_list)
                    }
            response = self.generator.generate(augmented_data=augmented_data)
            print(f"[*] LLM => {response}")



class WebRAG(RAG):
    def __init__(
            self,
            url_list,
            database_name,
            chunk_size=1000
            ):
        super().__init__()
        self.retrival = WebRetrival(
                database_name=database_name,
                url_list=url_list,
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

            result = self.retrival.get(query_text=prompt, result_count=10)
            response_list = result["documents"][0]

            augmented_data = {
                    "query" : prompt,
                    "context" : "\n".join(response_list)
                    }
            response = self.generator.generate(augmented_data=augmented_data)
            print(f"[*] LLM => {response}")


class NaiveRAG(RAG):
    def __init__(self, dir_path, retrivel_method, chunk_size=1000):
        super().__init__()

        if retrivel_method == "keyword":
            self.retrival = NaiveKeywordRetrival(
                    dir_path=dir_path,
                    chunk_size=chunk_size
                    )

        elif retrivel_method == "vectorize":
            self.retrival = NaiveVectorizeRetrival(
                    dir_path=dir_path,
                    chunk_size=chunk_size
                    )
        else:
            raise RuntimeError(f"Unknown retrival method {retrivel_method}")

        self.generator = CorpusResponseGenerator()

        print(f"[*] Naive RAG {retrivel_method}")



    def run(self):
        running = True
        while running:
            prompt = input(">>> ")
            if prompt == "exit":
                running = False
                continue

            response_list = self.retrival.get(query_text=prompt, result_count=10)

            augmented_data = {
                    "query" : prompt,
                    "context" : "\n".join(response_list)
                    }
            response = self.generator.generate(augmented_data=augmented_data)
            print(f"[*] LLM => {response}")










