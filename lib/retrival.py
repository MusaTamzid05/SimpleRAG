

class Retrival:
    def __init__(self):
        pass

    def get(self, query):
        raise RuntimeError("Not implemented")


class CorpusRetrival(Retrival):
    def __init__(self, path, chunk_size):
        super().__init__()
        corpus_text = ""

        with open(path, "r") as f:
            corpus_text = f.read()


        chunks = []

        for index in range(0, len(corpus_text), chunk_size):
            text = corpus_text[index:index+chunk_size]
            chunks.append(text)

        print(f"[*] Total chunks {len(chunks)}")





