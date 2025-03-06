from lib.database import ChromaDB
from lib.text_preprocessor import SimpleTextPreprocessor
from lib.utils import SimpleDirFileReader
from lib.vectorizer import DocumentVectorizer
import numpy as np
import faiss
import requests
from bs4 import BeautifulSoup


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



class IndexRetrival(Retrival):
    def __init__(self, dir_path, chunk_size):
        super().__init__()

        dir_reader = SimpleDirFileReader(dir_path=dir_path)
        text_list = dir_reader.read()
        text_preprocessor = SimpleTextPreprocessor()

        print(f"[*] Total text_list for index retrival {len(text_list)}")
        documents = []

        for text in text_list:
            if len(text) <= chunk_size:
                processed_text = text_preprocessor.run(text=text)
                documents.append(processed_text)

            else:
                for i in range(0, len(text), chunk_size):
                    chunk = text[i:i+chunk_size]
                    processed_text = text_preprocessor.run(text=chunk)
                    documents.append(processed_text)

        print(f"[*] Total docs for index retrival {len(documents)}")

        self.vectorizer = DocumentVectorizer()
        self.vectorizer.load_data(src=documents)

        embedded_data  = self.vectorizer.vectorize()
        embedded_data = np.array(embedded_data).astype("float32")
        dimention = embedded_data.shape[1]

        self.index = faiss.IndexFlatL2(dimention)
        self.index.add(embedded_data)

        self.documents = documents







    def get(self, query_text, result_count):
        vectorize_query = self.vectorizer.vectorize_text(texts=[query_text])
        vectorize_query = np.array(vectorize_query).astype("float32")
        _, indices = self.index.search(vectorize_query, k=result_count)
        results = [self.documents[index] for index in indices[0]]

        return results




class WebRetrival(Retrival):
    def __init__(self, url_list, database_name,  chunk_size=1000):
        super().__init__()
        self.documents = []
        text_preprocessor = SimpleTextPreprocessor()

        for url in url_list:
            print(f"[*] Getting {url}")
            res = requests.get(url)

            if res.status_code != 200:
                print(f"[X] Error getting {url}")
                continue

            soup = BeautifulSoup(res.content, "html.parser")
            text = soup.get_text()
            processed_text = text_preprocessor.run(text=text)

            if len(processed_text) <= chunk_size:
                self.documents.append(processed_text)
            else:
                for i in range(0, len(processed_text), chunk_size):
                    chunk = text[i:i+chunk_size]
                    self.documents.append(chunk)


            print(f"[*] Total documents {len(self.documents)}")

            self.database = ChromaDB(name=database_name)
            self.database.add(documents=self.documents)



    def get(self, query_text, result_count):
        return self.database.get_match(
                query_text=query_text,
                result_count=result_count
                )




