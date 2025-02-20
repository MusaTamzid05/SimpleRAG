from lib.database import ChromaDB
from lib.text_preprocessor import SimpleTextPreprocessor

class Retrival:
    def __init__(self):
        pass

    def get(self, query, result_count):
        raise RuntimeError("Not implemented")


class CorpusRetrival(Retrival):
    def __init__(self, database_name, path, chunk_size):
        super().__init__()
        corpus_text = ""

        with open(path, "r") as f:
            corpus_text = f.read()


        chunks = []
        text_preprocessor = SimpleTextPreprocessor()



        for index in range(0, len(corpus_text), chunk_size):
            text = corpus_text[index:index+chunk_size]
            processed_text = text_preprocessor.run(text=text)
            chunks.append(processed_text)

        print(f"[*] Total chunks {len(chunks)}")

        self.database = ChromaDB(name=database_name)
        self.database.add(documents=chunks)




    def get(self, query_text, result_count):
        return self.database.get_match(
                query_text=query_text,
                result_count=result_count
                )



