from lib.retrival import IndexRetrival

def main():
    rag = IndexRetrival(dir_path="data", chunk_size=1000)
    docs = rag.get(query_text="who is alice ?", result_count=5)

    for doc in docs:
        print(doc)
        print("-" * 30)






if __name__ == "__main__":
    main()

