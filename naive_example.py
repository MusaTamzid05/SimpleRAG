from lib.rag import NaiveRAG

def working1():
    rag = NaiveRAG(dir_path="data", chunk_size=1000, retrivel_method="keyword")
    rag.run()


def working2():
    rag = NaiveRAG(dir_path="data", chunk_size=1000, retrivel_method="vectorize")
    rag.run()


def main():
    working2()


if __name__ == "__main__":
    main()

