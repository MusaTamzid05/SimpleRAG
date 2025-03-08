from lib.rag import NaiveRAG

def main():
    rag = NaiveRAG(dir_path="data", chunk_size=1000, retrivel_method="keyword")
    rag.run()





if __name__ == "__main__":
    main()

