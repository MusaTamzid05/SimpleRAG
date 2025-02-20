import chromadb

class VectorDataBase:
    def __init__(self, name):
        self.name = name

    def add(self, document):
        raise RuntimeError("Not implemented")

    def get_match(self, query_text, result_count):
        raise RuntimeError("Not implemented")



class ChromaDB(VectorDataBase):
    def __init__(self, name):
        super().__init__(name=name)
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(name=name)


    def add(self, documents):
        self.collection.upsert(documents=documents, ids=[str(index) for index in range(len(documents))])


    def get_match(self, query_text, result_count):
        return self.collection.query(query_texts=[query_text], n_results=result_count)



if __name__ == "__main__":
    database = ChromaDB(name="test")
    documents = [
            "I like apple",
            "Drive to office yesterday",
            "Sky is not always blue"
            ]

    database.add(documents=documents)
    result = database.get_match(query_text="I like orange", result_count=2)

    print(result["documents"][0])


