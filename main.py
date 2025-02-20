from lib.rag import CorpusRAG

def main():
    rag = CorpusRAG(path="data/alice.txt", chunk_size=1000, database_name="alice")
    rag.run()





if __name__ == "__main__":
    main()

