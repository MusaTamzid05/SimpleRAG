from lib.rag import CorpusIndexRAG

def main():
    rag = CorpusIndexRAG(dir_path="data", chunk_size=1000)
    rag.run()






if __name__ == "__main__":
    main()

