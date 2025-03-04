from sentence_transformers import SentenceTransformer

class Vectorizer:
    def __init__(self):
        pass

    def load_data(self, src):
        # this src can be anything, from path to list 
        raise RuntimeError("Not implemented")

    def vectorize(self):
        raise RuntimeError("Not implemented")





class DocumentVectorizer(Vectorizer):
    def __init__(self):
        super().__init__()
        self.model = SentenceTransformer("all-MiniLM-L6-v2")


    def load_data(self, src):
        if isinstance(src, list) == False:
            src = [src]
        self.documents = src


    def vectorize(self):
        return self.model.encode(self.documents).tolist()

    def vectorize_text(self, texts):
        if isinstance(texts, list) == False:
            texts = [texts]
        
        return self.model.encode(self.documents).tolist()



